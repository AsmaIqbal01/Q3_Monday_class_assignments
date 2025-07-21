import chainlit as cl
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI,RunConfig
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"

)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model= model,
    model_provider=external_client,
    tracing_disabled= False
)

agent=Agent(
    name = "Smart Store Agent",
    instructions="""
            You are a helpful Smart Store Agent. 
    Ask customers what they are looking for and guide them with personalized product suggestions. 
    Explain benefits based on their described needs, like skin type, budget, or preferences.
    """
)

conversation_history =[]
@cl.on_message
async def welcome_message():
      welcome_text="Welcome to the Smart Store! I'm here to help you find the perfect products based on your needs. Please tell me what you're looking for!"
                   
      await cl.Message(content = welcome_text).send()

@cl.on_message
async def handle_message(message:cl.Message):
    global conversation_history
    conversation_history.append({"role":"user","content":message.content})    
    result =Runner.run_sync(
        agent,
        input = message.content,
        run_config=config
    )

    conversation_history.append({"role":"assistant","content":result.final_output})
    await cl.Message(content=result.final_output).send()