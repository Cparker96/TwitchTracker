from dotenv import load_dotenv
from auth import fetch_token
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
    
# def set_subscribe(message_id: str, token: str, user: dict):
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Client-Id": client_id,
#         "Content-Type": "application/json"
#     }

#     sub_data = {
#         "type": "stream.online",
#         "version": "1",
#         "condition": {
#             "broadcaster_id": user['data'][0]['id']
#         },
#         "transport": {
#             "method": "websocket"
#         }

#     }

#     subscribe = requests.post(url=stream_url + "/eventsub/subscriptions")

# def get_users(token: str, streamer_list: list) -> dict:
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Client-Id": client_id,
#     }

#     for streamer in streamer_list:
#         users = requests.get(url=stream_url + f"/users?login={streamer}", headers=headers)
#         return users.json()

def get_streams(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": client_id
    }

    streams = requests.get(url=stream_url + f"/streams?user_login=tenz&type=live", headers=headers)
    return streams.json()
