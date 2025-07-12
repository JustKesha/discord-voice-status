import requests
from enum import Enum
from utils import config

class CustomStatus(Enum):
    ONLINE = "online"
    IDLE = "idle"
    DND = "dnd"
    INVISIBLE = "invisible"

class Default:
    STATUS = CustomStatus.ONLINE

def send_payload(discord_token: str, payload: dict) -> dict:
    api = config["api"]
    discord_api_url = api["discord_url"] + api["discord_settings"]
    response = requests.patch(
        discord_api_url,
        headers = {
            "Authorization": discord_token,
            "User-Agent": api["user_agent"],
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        json = payload
    )
    return response.json()

def set_custom_status(
        discord_token: str,
        message: str,
        emoji: str,
        status: CustomStatus = Default.STATUS
        ) -> dict:
    return send_payload(discord_token, {
        "custom_status": {
            "text": message,
            "emoji_name": emoji,
        },
        "status": status.value
    })