from occupancy_monitor import occupancy_selenium_monitor
from weather_monitor import weather_selenium_monitor
from dotenv import load_dotenv
import pytz

# This program is used to test the DB, by extracting one instance of the data using the selenium webscraper, then inserting it into the DB

from datetime import datetime, timezone
import os
from regexExtractor import extractor

def retrieveCurrentData():
    load_dotenv()

    # Initialize occupancy driver and extract occupancy text
    occupancy_driver = occupancy_selenium_monitor()
    occupancy_element = occupancy_driver.find_element(by='xpath', value=os.getenv('OCCUPANCY_XPATH'))
    occupancy_text = occupancy_element.text

    # Initialize weather driver and extract weather data
    weather_driver = weather_selenium_monitor()

    # temperature (C)
    tempPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[1]/span'
    temp_text = weather_driver.find_element(by='xpath', value=(tempPath)).text

    # humidity (%)
    humidityPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[2]/ul/li[1]/div/span[2]'
    humidity_text = weather_driver.find_element(by='xpath', value=(humidityPath)).text

    # chance_of_rain (%)
    rainPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[3]/div[1]/span'
    rain_text = weather_driver.find_element(by='xpath', value=(rainPath)).text

    # wind (MPH)
    windPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[3]/div[2]/span/span[2]'
    wind_text = weather_driver.find_element(by='xpath', value=(windPath)).text

    # Extract occupancy percentage and prepare to insert data into the database
    percentage_value = extractor(occupancy_text)

    # Define the timezone
    tz = pytz.timezone('Europe/London')
    
    # Get the current time and date in BST (Brittish Summer Time)
    current_time_bst = datetime.now(tz).strftime('%H:%M')
    current_day_bst = datetime.now(tz).strftime('%A')
    current_date_bst = datetime.now(tz).strftime('%Y-%m-%d')

    # Cleanup
    occupancy_driver.quit()
    weather_driver.quit()

    return {
        'occupancy_percentage': percentage_value,
        'time': current_time_bst,
        'day_of_week': current_day_bst,
        'date': current_date_bst,
        'temperature': temp_text,
        'humidity': humidity_text,
        'chance_of_rain': rain_text,
        'wind_speed': wind_text
    }


if __name__ == "__main__":
    main()