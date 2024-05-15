from auth import fetch_token
from users import get_streams
from drivers import init_driver, locate_channel_button
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

        for stream in get_stream_status["data"]:
            driver = init_driver()
            if driver.current_url == f"https://twitch.tv/{stream['user_login']}":
                claim_button = locate_channel_button(driver)
                if claim_button is not None:
                    claim_button.click()
asyncio.run(main())

