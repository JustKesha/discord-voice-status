import requests

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
        custom_status: str,
        emoji: str,
        status: str = "online" # TODO Should be enum (online/idle/dnd/invisible)
        ) -> dict:
    return send_payload(discord_token, {
        "custom_status": {
            "text": custom_status,
            "emoji_name": emoji,
        },
        "status": status
    })