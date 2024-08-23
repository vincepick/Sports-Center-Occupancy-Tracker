import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os

# Returns selenium web driver for weather information
def weather_selenium_monitor():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')  # Run in headless mode

    web = os.getenv('WEB_PATH_WEATHER')
    path=os.getenv('DRIVER_PATH')
    service=Service(executable_path=path)
    driver = webdriver.Chrome(service=service)



    driver.get(web)

    return driver