from auth import fetch_token
from users import get_streams
from drivers import init_driver, locate_channel_button
from queue import Queue
from threading import Thread
import asyncio
import requests
import time

async def main():
    token = fetch_token()
    ### I'm gonna need to figure out how to recursively check to see if the token is valid
    ### not solving for it now

    while True:
        try:      
            get_stream_status = get_streams(token["access_token"])
            if len(get_stream_status["data"]) == 0:
                # check in one minute if streamer is live again
                time.sleep(60)
                continue

            if get_stream_status["data"][0]["viewer_count"] > 0:
                break
        except requests.exceptions.ConnectionError as connError:
            print(f"connection issue raised - {connError}")
            break
            # check if status code is 401 - refresh the token if true
        except requests.exceptions.HTTPError as httpError:
            if httpError.response.status_code == 401:
                token = fetch_token()
                continue
            print(f"unsuccessful response not due to auth - {httpError.response.json()}")
            break
        # if no streamers are returned, continue the endless loop
        if get_stream_status['data'] is None:
            time.sleep(10)
            continue
    
    driver = init_driver()
    if driver.current_url == f"https://twitch.tv/{get_stream_status['data'][0]['user_login']}":
        claim_button = locate_channel_button(driver)
        return claim_button

asyncio.run(main())

