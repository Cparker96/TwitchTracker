from dotenv import load_dotenv
import websockets
import json
import requests
import os

load_dotenv()
client_id = os.getenv("CLIENT_ID")

async def init_socket():
    async with websockets.connect("wss://eventsub.wss.twitch.tv/ws") as websocket:
        await websocket.send("ping")
        message = await websocket.recv()
        recv_message = json.loads(message)
        return recv_message['metadata']['message_id']
    
def set_subscribe(message_id: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id,
        "Content-Type": "application/json"
    }

    sub_data = {
        "type": "stream.online",
        "version": "1",

    }

    subscribe = requests.post("https://api.twitch.tv/helix/eventsub/subscriptions")

def get_users(token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id,
    }

    users = requests.get("https://api.twitch.tv/helix/users?login=loltyler1")
    return users.json()