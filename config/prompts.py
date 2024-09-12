from pathlib import Path

from pydantic import BaseModel

from config.utils import create_and_validate_config


PROMPTS_FILE_PATH = Path(__file__).resolve().parent.parent / "prompts.yaml"


class Prompt(BaseModel):
    prompt: str
    expected_output: str


class Prompts(BaseModel):
    explorer: Prompt
    writer: Prompt
    humanizer: Prompt
    translator: Prompt


prompts = create_and_validate_config(
    master_cls=Prompts, cfg_path=PROMPTS_FILE_PATH)
