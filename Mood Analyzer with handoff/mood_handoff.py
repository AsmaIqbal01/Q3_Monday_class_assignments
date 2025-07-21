from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig, handoff
from openai import AsyncOpenAI
from dotenv import load_dotenv
import asyncio
import os

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("Gemini API key is not set.")

# Setup Gemini API client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model setup
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Run configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Activity Advisor Agent
activity_agent = Agent(
    name="Activity Advisor Agent",
    model=model,
    instructions="""
        You are a helpful assistant. 
        Suggest a calming or uplifting activity for someone who is feeling sad or stressed.
    """
)

# Mood Analyzer Agent with internal logic for handoff
class MoodAnalyzerAgent(Agent):
    async def handle(self, input: str, config: RunConfig):
        result = await self.model.complete(
            prompt=f"Determine the user's mood from this message: {input}\nOnly respond with one word: Happy, Sad, Stressed, Angry, or Neutral.",
            config=config
        )
        mood = result.strip().lower()

        if mood in ["sad", "stressed"]:
            return handoff(
                agent=activity_agent,
                input=f"The user is feeling {mood}. Suggest something helpful.",
                output=mood
            )
        return mood.capitalize()

# Use the custom MoodAnalyzerAgent
mood_agent = MoodAnalyzerAgent(
    name="Mood Analyzer Agent",
    model=model,
    instructions="Analyze mood and hand off if necessary."
)

# Main async function
async def main():
    user_input = input("How are you feeling today?\n")
    result = await Runner.run(mood_agent, user_input)
    if hasattr(result,'handoff_call'):
        print("Detected Mood:", result.handoff_call.input)
        print("Suggested Activity:", result.handoff_call.output.strip())
    else:
        print("Detected Mood:", result.handoff_call.input)

        print("No activity suggestion needed.")

# Run
asyncio.run(main())
