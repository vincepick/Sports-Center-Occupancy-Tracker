from occupancy_monitor import occupancy_selenium_monitor
from weather_monitor import weather_selenium_monitor
from dotenv import load_dotenv
import pytz

# This program is used to test the DB, by extracting one instance of the data using the selenium webscraper, then inserting it into the DB

from datetime import datetime, timezone
import os
from regexExtractor import extractor
import sqlite3

def main():
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

    # Open sqlite connection
    conn = sqlite3.connect('occupancy_data/gym_occupancy_data.db')
    cursor = conn.cursor()

    # Insert data into the database
    cursor.execute("INSERT INTO occupancy_data (percentage_column, bst_time, day_of_week, current_date_bst, temperature, humidity, chance_of_rain, wind) VALUES (?,?,?,?,?,?,?,?)", 
                   (percentage_value, current_time_bst, current_day_bst, current_date_bst, temp_text, humidity_text, rain_text, wind_text))

    conn.commit()
    conn.close()

    # Cleanup
    occupancy_driver.quit()
    weather_driver.quit()


if __name__ == "__main__":
    main()