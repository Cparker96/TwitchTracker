from dotenv import load_dotenv
import http.client, urllib
import os

load_dotenv()
api_key = os.getenv("PUSHOVER_API_KEY")
user_key = os.getenv("PUSHOVER_USER_KEY")

def send_message(api_key: str, user_key: str):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": api_key,
        "user": user_key,
        "message": "hello world",
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()