import pytz
from datetime import datetime
from chromeSetup import get_chrome_driver
from scraper import scrape_occupancy, scrape_weather
from database import insert_data_to_db

def lambda_handler(event, context):
    driver = None
    try:
        driver = get_chrome_driver()

        occupancy_number = scrape_occupancy(driver)
        temp_text, humidity_text, rain_text, wind_text = scrape_weather(driver)

        tz = pytz.timezone('Europe/London')
        current_time_bst = datetime.now(tz).strftime('%H:%M')
        current_day_bst = datetime.now(tz).strftime('%A')
        current_date_bst = datetime.now(tz).strftime('%Y-%m-%d')

        insert_data_to_db(occupancy_number, current_time_bst, current_day_bst, current_date_bst, temp_text, humidity_text, rain_text, wind_text)
    
    finally:
        if driver:
            driver.quit()
