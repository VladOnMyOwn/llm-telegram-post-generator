from pathlib import Path
from typing import Optional, Type

from pydantic import BaseModel
from strictyaml import YAML, load


def fetch_config_from_yaml(cfg_path: Path) -> YAML:

    if not cfg_path.is_file():
        raise FileNotFoundError(f"Config not found at {cfg_path}")

    with open(cfg_path, "r") as config_file:
        parsed_config = load(config_file.read())

        return parsed_config


def create_and_validate_config(
        master_cls: BaseModel,
        parsed_config: Optional[YAML] = None,
        cfg_path: Optional[Path] = None
) -> Type[BaseModel]:

    if parsed_config is None:
        if cfg_path is not None:
            parsed_config = fetch_config_from_yaml(cfg_path)
        else:
            raise TypeError("parsed_config or cfg_path must be specified")

    config = master_cls(**parsed_config.data)

    return config
