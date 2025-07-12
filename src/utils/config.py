import os
from pathlib import Path
from typing import Dict, Any
import yaml
from dotenv import load_dotenv

DEFAULT_ROOT = Path(__file__).parent.parent.parent
DEFAULT_YAML = "config.yaml"
DEFAULT_ENVS = ".env"
DEFAULT_ENVS_PREFIX = "PY_TDS_"
DEFAULT_ENVS_SECTION = "env"

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

def merge_envs_to_config(
        config: Dict[str, Any],
        envs: os._Environ[str],
        prefix: str = DEFAULT_ENVS_PREFIX,
        config_section: str = DEFAULT_ENVS_SECTION,
        remove_prefix: bool = True
        ) -> Dict[str, Any]:
    env_config = {
        (k[len(prefix):] if remove_prefix else k): v
        for k, v in envs.items() if k.startswith(prefix)
        }
    if config_section and env_config:
        config[config_section] = env_config
        return config
    else:
        return {**config, **env_config}

def load_config(
        yaml_file: str = DEFAULT_YAML,
        envs_file: str = DEFAULT_ENVS,
        root_path: str = DEFAULT_ROOT, # NOTE Using same path for yaml & envs
        envs_prefix: str = DEFAULT_ENVS_PREFIX,
        envs_section: str = DEFAULT_ENVS_SECTION,
        envs_remove_prefix: bool = True
        ) -> Dict[str, Any]:
    return merge_envs_to_config(
        config = load_yaml(yaml_file, root_path),
        envs = load_envs(envs_file, root_path),
        prefix = envs_prefix,
        config_section = envs_section,
        remove_prefix = envs_remove_prefix
        )