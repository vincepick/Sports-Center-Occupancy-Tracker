import pytz
from datetime import datetime
from chromeSetup import get_chrome_driver
from scraper import scrape_occupancy, scrape_weather
from database import insert_data_to_db

# The function that is actually called with each iteration of the lambda function
def lambda_handler(event, context):
    # Initializing early so can use in try catch later
    driver = None
    try:
        # retrieving chrome driver
        driver = get_chrome_driver()

        # retrieving web scraping results
        occupancy_number = scrape_occupancy(driver)
        temp_text, humidity_text, rain_text, wind_text = scrape_weather(driver)

        tz = pytz.timezone('Europe/London')
        current_time_bst = datetime.now(tz).strftime('%H:%M')
        current_day_bst = datetime.now(tz).strftime('%A')
        current_date_bst = datetime.now(tz).strftime('%Y-%m-%d')

        # inserting the scraped data
        insert_data_to_db(occupancy_number, current_time_bst, current_day_bst, current_date_bst, temp_text, humidity_text, rain_text, wind_text)
    
    finally:
        if driver:
            driver.quit()
