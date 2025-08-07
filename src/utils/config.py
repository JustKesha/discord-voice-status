import os
from pathlib import Path
from typing import Dict, Any, TypedDict, Literal, Optional
import yaml
from dotenv import load_dotenv

class ConfigStatus(TypedDict):
    language: str # ISO 639 language code
    emoji: str # Unicode emoji or custom Discord emoji
    update_interval: float # Seconds
    filter: Literal["on", "off"] # Naughty words filter
    censor_mode: Literal["full", "first_last_visible", "first_visible"]

class ConfigRecording(TypedDict):
    device_index: Optional[int] # Set to null to use default mic, otherwise 0-N

class ConfigApiUrl(TypedDict):
    base: str
    settings: str

class ConfigApiLimits(TypedDict):
    max_custom_status_length: int
    presence_update_rate_limit: int # Seconds

class ConfigApi(TypedDict):
    url: ConfigApiUrl
    user_agent: str
    limits: ConfigApiLimits

class ConfigEnv(TypedDict):
    DISCORD_TOKEN: str

class Config(TypedDict):
    status: ConfigStatus
    recording: ConfigRecording
    env: ConfigEnv
    api: ConfigApi

class Default:
    ROOT: Path = Path(__file__).parent.parent.parent
    YAML: str = "config.yaml"
    ENVS: str = ".env"
    ENVS_PREFIX: str = "PY_DVS_"
    ENVS_SECTION: str = "env"
    ENVS_REMOVE_PREFIX: bool = True
    ENCODING: str = "utf-8"

config: Config = None

def load_yaml(
        name: str = Default.ROOT,
        path: Path = Default.ROOT,
        encoding: str = Default.ENCODING
        ) -> Config:
    # TODO Add config structure validation & fallback values
    with open(path / name, mode="r", encoding=encoding) as f:
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
        ) -> Config:
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
        ) -> Config:
    global config
    config = merge_envs_to_config(
        config = load_yaml(yaml_file, root_path),
        envs = load_envs(envs_file, root_path),
        **kwargs
        )
    return config

def get_config() -> Config: return config

if __name__ == "__main__":
    load_config()