import os
from pathlib import Path
from typing import Dict, Any
import yaml
from dotenv import load_dotenv

DEFAULT_ROOT = Path(__file__).parent.parent.parent
DEFAULT_YAML = "config.yaml"
DEFAULT_ENVS = ".env"

def load_yaml(
        name: str = DEFAULT_YAML,
        path: Path = DEFAULT_ROOT
        ) -> Dict[str, Any]:
    with open(path / name) as f:
        data = yaml.safe_load(f)
    return data

def load_envs(
        name: str = DEFAULT_ENVS,
        path: Path = DEFAULT_ROOT
        ) -> os._Environ[str]:
    load_dotenv(path / name)
    return os.environ

def load_config(
        yaml_file: str = DEFAULT_YAML,
        envs_file: str = DEFAULT_ENVS,
        root_path: str = DEFAULT_ROOT, # NOTE Using same path for yaml & envs
        ) -> Dict[str, Any]:
    return {**load_yaml(yaml_file, root_path), **load_envs(envs_file, root_path)}