import requests
from enum import Enum

class CustomStatus(Enum):
    ONLINE = "online"
    IDLE = "idle"
    DND = "dnd"
    INVISIBLE = "invisible"

def send_payload(discord_token: str, payload: dict) -> dict:
    response = requests.patch(
        "https://discord.com/api/v9/users/@me/settings",
        headers = {
            "Authorization": discord_token,
            "Content-Type": "application/json",
        },
        json = payload
    )

    return response.json()

def set_custom_status(
        discord_token: str,
        message: str,
        emoji: str,
        status: CustomStatus = CustomStatus.ONLINE
        ) -> dict:
    return send_payload(discord_token, {
        "custom_status": {
            "text": message,
            "emoji_name": emoji,
        },
        "status": status.value
    })