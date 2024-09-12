from pathlib import Path

from pydantic import BaseModel

from config.utils import create_and_validate_config


CONFIG_FILE_PATH = Path(__file__).resolve().parent.parent / "config.yaml"


class ModelConfig(BaseModel):
    name: str
    temperature: float
    max_tokens: int


class Config(BaseModel):
    topic: str
    output_file: str
    model: ModelConfig


config = create_and_validate_config(
    master_cls=Config, cfg_path=CONFIG_FILE_PATH)
