from dotenv import load_dotenv
import websockets
import json
import requests
import os

load_dotenv()
client_id = os.getenv("CLIENT_ID")
stream_url = "https://api.twitch.tv/helix"

async def init_socket():
    async with websockets.connect("wss://eventsub.wss.twitch.tv/ws") as websocket:
        await websocket.send("ping")
        message = await websocket.recv()
        recv_message = json.loads(message)
        return recv_message['metadata']['message_id']

def get_streams(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id
    }

    streams = requests.get(url=stream_url + f"/streams?user_login=tenz&type=live", headers=headers)
    return streams.json()
