from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()
client_id = os.getenv("CLIENT_ID")
stream_url = "https://api.twitch.tv/helix"

def get_streams(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id
    }

    streams = requests.get(url=stream_url + f"/streams?user_login=tenz&type=live", headers=headers)
    return streams.json()
