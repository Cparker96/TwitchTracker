from selenium import webdriver
from selenium.webdriver.common.by import By
import Chrome
import time
def init_driver(streamer: str):
    # add option flags to bypass tbsCertificate error
    driver_path = r'''C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'''
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.ChromeService(executable_path=driver_path)
    browser.start()
    # browser.get(f"https://twitch.tv/{streamer}")
    return browser
    
def locate_channel_button(driver: webdriver):
    claim_button = driver.find_element(By.CLASS_NAME, "ScCoreButton-sc-ocjdkq-0").click()
    return claim_button

if __name__ == "__main__":
    s = init_driver('averagejonas')
    #a = locate_channel_button(s)
    print(s)