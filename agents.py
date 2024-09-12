import os

from crewai import Agent
from dotenv import find_dotenv, load_dotenv
from groq import DefaultHttpxClient
from langchain_groq import ChatGroq

from config.agents import agents
from config.core import config


_ = load_dotenv(find_dotenv())

# proxying access to avoid region limitations
http_client = DefaultHttpxClient(
    verify=False,
    proxy=os.environ.get("HTTP_PROXY")
)

model = config.model.name
# tokens_per_min = 5000  # https://console.groq.com/settings/limits
temperature = config.model.temperature
max_tokens = config.model.max_tokens

llm_client = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    http_client=http_client,
    model=model,
    temperature=temperature,
    max_tokens=max_tokens
)

# create agents
data_researcher = Agent(
    role=agents.explorer.role,
    goal=agents.explorer.goal,
    verbose=True,
    memory=False,
    backstory=agents.explorer.backstory,
    llm=llm_client,
    allow_delegation=False,
)

telegram_post_writer = Agent(
    role=agents.writer.role,
    goal=agents.writer.goal,
    verbose=True,
    memory=False,
    backstory=agents.writer.backstory,
    llm=llm_client,
    allow_delegation=False,
)

humanizer_agent = Agent(
    role=agents.humanizer.role,
    goal=agents.humanizer.goal,
    verbose=True,
    memory=False,
    backstory=agents.humanizer.backstory,
    llm=llm_client,
    allow_delegation=False,
)

translator_agent = Agent(
    role=agents.translator.role,
    goal=agents.translator.goal,
    verbose=True,
    memory=True,
    backstory=agents.translator.backstory,
    llm=llm_client,
    allow_delegation=False,
)
