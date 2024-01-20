from dotenv import load_dotenv
import requests
import os

load_dotenv()
auth_url = "https://id.twitch.tv"
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def fetch_token() -> str:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
    }

    post_token = requests.post(url=auth_url + '/oauth2/token', headers=headers, data=data)
    token = post_token.json()
    return token