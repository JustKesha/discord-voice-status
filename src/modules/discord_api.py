import time
import requests
from enum import Enum
from utils import get_config

class CustomStatus(Enum):
    ONLINE = "online"
    IDLE = "idle"
    DND = "dnd"
    INVISIBLE = "invisible"

class Default:
    STATUS: CustomStatus = CustomStatus.ONLINE
    EMOJI: str = ""

_last_api_call_time = 0
_payload_rate_limit = 0 # Max 1 call per <- seconds

def can_send_payload() -> bool:
    global _last_api_call_time, _payload_rate_limit
    config = get_config()
    api = config["api"]
    # TODO Add init() method to update _payload_rate_limit
    # instead of having it update each payload send
    _payload_rate_limit = api["limits"]["presence_update_rate_limit"]

    current_time = time.time()
    time_since_last_call = current_time - _last_api_call_time

    if time_since_last_call < _payload_rate_limit:
        return False
    
    _last_api_call_time = current_time
    return True

def send_payload(payload: dict) -> dict:
    if not can_send_payload():
        return {}

    config = get_config()
    api = config["api"]
    discord_api_url = api["url"]["base"] + api["url"]["settings"]
    response = requests.patch(
        discord_api_url,
        headers = {
            "Authorization": config["env"]["DISCORD_TOKEN"],
            "User-Agent": api["user_agent"],
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        json = payload
    )
    return response.json()

def set_custom_status(
        message: str,
        emoji: str = Default.EMOJI,
        status: CustomStatus = Default.STATUS
        ) -> dict:
    config = get_config()
    limits = config["api"]["limits"]
    message = message[:limits["max_custom_status_length"]]
    return send_payload({
        "custom_status": {
            "text": message,
            "emoji_name": emoji,
        },
        "status": status.value
    })