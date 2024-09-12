from pathlib import Path

from pydantic import BaseModel

from config.utils import create_and_validate_config


AGENTS_FILE_PATH = Path(__file__).resolve().parent.parent / "agents.yaml"


class Agent(BaseModel):
    role: str
    goal: str
    backstory: str


class Agents(BaseModel):
    explorer: Agent
    writer: Agent
    humanizer: Agent
    translator: Agent


agents = create_and_validate_config(
    master_cls=Agents, cfg_path=AGENTS_FILE_PATH)
