import os
from pathlib import Path
from typing import Dict, Any, Union
import yaml
from dotenv import load_dotenv

config: Union[Dict[str, Any], None] = None

class Default:
    ROOT = Path(__file__).parent.parent.parent
    YAML = "config.yaml"
    ENVS = ".env"
    ENVS_PREFIX = "PY_DVS_"
    ENVS_SECTION = "env"
    ENVS_REMOVE_PREFIX = True

def load_yaml(
        name: str = Default.ROOT,
        path: Path = Default.ROOT
        ) -> Dict[str, Any]:
    with open(path / name) as f:
        data = yaml.safe_load(f)
    return data

def load_envs(
        name: str = Default.ENVS,
        path: Path = Default.ROOT
        ) -> os._Environ[str]:
    load_dotenv(path / name)
    return os.environ

def merge_envs_to_config(
        config: Dict[str, Any],
        envs: os._Environ[str],
        prefix: str = Default.ENVS_PREFIX,
        config_section: str = Default.ENVS_SECTION,
        remove_prefix: bool = Default.ENVS_REMOVE_PREFIX
        ) -> Dict[str, Any]:
    env_config = {
        # TODO Add option to lowercase env names for config
        (k[len(prefix):] if remove_prefix else k): v
        for k, v in envs.items() if k.startswith(prefix)
        }
    if config_section and env_config:
        config[config_section] = env_config
        return config
    else:
        return {**config, **env_config}

def load_config(
        yaml_file: str = Default.YAML,
        envs_file: str = Default.ENVS,
        root_path: str = Default.ROOT, # NOTE Using same path for yaml & envs
        **kwargs
        ) -> Dict[str, Any]:
    global config
    config = merge_envs_to_config(
        config = load_yaml(yaml_file, root_path),
        envs = load_envs(envs_file, root_path),
        **kwargs
        )
    return config

def get_config() -> Dict[str, Any]: return config

if __name__ == "__main__":
    load_config()