from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException
from dotenv import load_dotenv
import time
import os

load_dotenv()
unique_id = os.getenv("UNIQUE_ID")
exp_override = os.getenv("EXP_OVERRIDES")
auth_id = os.getenv("AUTH_ID")
persistent = os.getenv("PERSISTENT")
sudo = os.getenv("BITS_SUDO")
api_token_header = os.getenv("API_TOKEN_HEADER")
twilight_user = os.getenv("TWILIGHT_USER")
auth_token_header = os.getenv("AUTH_TOKEN_HEADER")
twilight_user_dev = os.getenv("TWILIGHT_USER_DEV")
tachyon_user = os.getenv("TACHYON_USER")
ga_60k = os.getenv("GA_60K")
ga_rzg = os.getenv("GA_RZG")
ga = os.getenv("GA")
gid = os.getenv("GID")
ga_nqn = os.getenv("GA_NQN")
server_session_id = os.getenv("SERVER_SESSION_ID")

def init_driver() -> webdriver:
    # add option flags to bypass tbsCertificate error
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.twitch.tv/loltyler1")

    cookies = {
        "twitch.lohp.countryCode": "US",
        "unique_id": unique_id,
        "unique_id_durable": unique_id,
        "experiment_overrides": exp_override,
        "authy_id": auth_id,
        "persistent": persistent,
        "bits_sudo": sudo,
        "login": "a5yncio",
        "name": "a5yncio",
        "last_login": "2024-05-21T04:15:18Z",
        "api_token": api_token_header,
        "twilight-user": twilight_user,
        "auth-token": auth_token_header,
        "twilight-user.dev": twilight_user_dev,
        "language": "en",
        "tachyon-prefers-color-scheme": "dark-preferred",
        "tachyon-user": tachyon_user,
        "_ga_60KWEWG403": ga_60k,
        "unique_id": unique_id,
    }

    for cookie in cookies:
        driver.add_cookie({"name": cookie, "value": cookies[cookie]})
    
    driver.refresh()
    return driver

    
def locate_channel_button(driver: webdriver) -> bool:
    try:
        time.sleep(10)
        claim_button = driver.find_element(By.XPATH, "//*[@id='live-page-chat']/div/div/div[2]/div/div/section/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button")
        claim_button.click()
        time.sleep(10)
    except NoSuchAttributeException:
        return False
    return True

if __name__ == "__main__":
    a = init_driver()
    b = locate_channel_button(a)
    print(b)