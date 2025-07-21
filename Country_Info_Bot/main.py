from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig ,AsyncOpenAI
import os
from agents.tools import Tool
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client=AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Sub-agent1
capital_agent = Agent(
    name="CapitalAgent",
    instructions="Return only the capital city of the given country.",
    model=model
)

# Wrapper function
def capital_tool_func(country: str) -> str:
    result = Runner.run_sync(capital_agent, input=country, run_config=config)
    return result.final_output

# Convert to tool
capital_tool = Tool.from_function(
    name="CapitalTool",
    description="Returns the capital city using CapitalAgent",
    func=capital_tool_func
)


# Sub-agent2
language_agent = Agent(
    name="LanguageAgent",
    instructions="Return only the Language of the given country.",
    model=model
)

# Wrapper function
def language_tool_func(country: str) -> str:
    result = Runner.run_sync(language_agent, input=country, run_config=config)
    return result.final_output

# Convert to tool
language_tool = Tool.from_function(
    name="LanguageTool",
    description="Returns the Language using LanguageAgent",
    func=capital_tool_func
)

# Sub-agent3
population_agent = Agent(
    name="PopulationAgent",
    instructions="Return only the Population of the given country.",
    model=model
)

# Wrapper function
def population_tool_func(country: str) -> str:
    result = Runner.run_sync(population_agent, input=country, run_config=config)
    return result.final_output

# Convert to tool
population_tool = Tool.from_function(
    name="PopulationTool",
    description="Returns the Population using LanguageAgent",
    func=capital_tool_func
)


country_bot=Agent(
    name="CountryBot",
    instructions="""
    You are a country information assistant.
    Take a country name as input.
    Use the tools to gather:
    - its capital (from CapitalAgent)
    - its language(s) (from LanguageAgent)
    - its population (from PopulationAgent)
    Return all three as a short structured answer.
    """,
    tools=[capital_tool,language_tool,population_tool],
    model=model
)
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
    
)
country_name=input("Enter a country name: ")
result=Runner.run_sync(
    country_bot,
    input=country_name,
    run_config=config
)
# Run
country = input("Enter a country: ")
result = Runner.run_sync(country_bot, input=country, run_config=config)
print("✅ Result:\n", result.final_output)

