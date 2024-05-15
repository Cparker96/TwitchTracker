from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException
from dotenv import load_dotenv
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
    driver.get("https://www.twitch.tv/tenz")
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
        "last_login": "2024-01-20T04:30:31Z",
        "api_token": api_token_header,
        "twilight-user": twilight_user,
        "auth-token": auth_token_header,
        "twilight-user.dev": twilight_user_dev,
        "language": "en",
        "tachyon-prefers-color-scheme": "dark-preferred",
        "tachyon-user": tachyon_user,
        "_ga_60KWEWG403": ga_60k,
        "unique_id": unique_id,
        "_ga_RZGH9Y6L73": ga_rzg,
        "_ga": ga,
        "_ga_NQNWDWJXCP": ga_nqn,
        "proto": "HTTP/3",
        "_gid": gid,
        "server_session_id": server_session_id
    }

    # cookie_dict = {
    #     "_ga": "GA1.1.394826768.1705724992",
    #     "_ga_60KWEWG403": "GS1.1.1715740598.7.1.1715741383.60.0.0",
    #     "_ga_NQNWDWJXCP": "GS1.1.1705902693.3.1.1705903138.0.0.0",
    #     "_ga_RZGH9Y6L73": "GS1.1.1705901858.1.1.1705902107.0.0.0",
    #     "_gid": "GA1.2.1639408864.1715738298",
    #     "api_token": "e01664f1a555160feb96e6260d7127e8",
    #     "auth-token": "zc18leuxijzpqfb69wox9tmbirkdjb",
    #     "experiment-overrides": "{%22experiments%22:{}%2C%22disabled%22:[]}",
    #     "language": "en",
    #     "last_login": "2024-01-20T04:30:31Z",
    #     "login": "a5yncio",
    #     "name": "a5yncio",
    #     "persistent": "432482890%3A%3Azjljamccjzyjd3sxdzrwza76nj4n1v",
    #     "proto": "HTTP/2+alt",
    #     "server_session_id": "a956b862341b49178f400d7be3c62289",
    #     "tachyon-perfers-color-scheme": "dark-preferred",
    #     "tachyon-user": "%7B%22id%22%3A%22432482890%22%2C%22login%22%3A%22a5yncio%22%2C%22version%22%3A%221%22%7D",
    #     "twilight-user": "{%22authToken%22:%22zc18leuxijzpqfb69wox9tmbirkdjb%22%2C%22displayName%22:%22a5yncio%22%2C%22id%22:%22432482890%22%2C%22login%22:%22a5yncio%22%2C%22roles%22:{%22isStaff%22:false}%2C%22version%22:2}",
    #     "twilight-user.dev": "{%22authToken%22:%22gcc6breqvl6v79px8k8rm087jg17d7%22%2C%22displayName%22:%22a5yncio%22%2C%22id%22:%22432482890%22%2C%22login%22:%22a5yncio%22%2C%22roles%22:{%22isStaff%22:false}%2C%22version%22:2}",
    #     "twitch.lohp.countryCode": "US",
    #     "unique_id": "4e96dba134c063d4",
    #     "unique_id_durable": "4e96dba134c063d4"
    # }

    for cookie in cookies:
        driver.add_cookie({"name": cookie, "value": cookies[cookie]})
    
    driver.refresh()
    return driver

    
def locate_channel_button(driver: webdriver):
    try:
        claim_button = driver.find_element(By.CLASS_NAME, "ScCoreButton-sc-ocjdkq-0")
    except NoSuchAttributeException:
        return False
    return True

def get_cookies():
    pass

if __name__ == "__main__":
    a = init_driver()
    b = locate_channel_button(a)
    print(b)