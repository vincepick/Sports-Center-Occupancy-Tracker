import os
import time
import re
import pytz
import mysql.connector
from datetime import datetime, timezone

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from tempfile import mkdtemp

def lambda_handler(event, context):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
    chrome_options.add_argument(f"--data-path={mkdtemp()}")
    chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    chrome_options.add_argument("--remote-debugging-pipe")
    chrome_options.add_argument("--verbose")
    chrome_options.add_argument("--log-path=/tmp")
    chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

    try:
        service = Service(
            executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver",
            service_log_path="/tmp/chromedriver.log"
        )

        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
        # Open a webpage
        driver.get('https://sport.wp.st-andrews.ac.uk/')

        occupancy_element = driver.find_element(by='xpath', value='/html/body/main/section[2]/div/div/div[2]/h3[1]')
        occupancy_text = occupancy_element.text

        occupancy_number=0
    
        percentage = re.search(r'(\d+)%', occupancy_text)
        if percentage:
    # Extract the matched value (which is the percentage number)
            occupancy_number=  int(percentage.group(1))

        driver.get('https://weather.com/en-GB/weather/tenday/l/St+Andrews+Scotland?canonicalCityId=56d2f9aaa0f62e8898b3c962f4d833ef1e869b73de2ad388a77bb57fd885c73a')

         # temperature (C)
        tempPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[1]/span'
        temp_text = driver.find_element(by='xpath', value=(tempPath)).text

        # humidity (%)
        humidityPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[2]/ul/li[1]/div/span[2]'
        humidity_text = driver.find_element(by='xpath', value=(humidityPath)).text

        # chance_of_rain (%)
        rainPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[3]/div[1]/span'
        rain_text = driver.find_element(by='xpath', value=(rainPath)).text

        # wind (MPH)
        windPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[3]/div[2]/span/span[2]'
        wind_text = driver.find_element(by='xpath', value=(windPath)).text

        # Extract occupancy percentage and prepare to insert data into the database

        # Define the timezone
        tz = pytz.timezone('Europe/London')
        
        # Get the current time and date in BST (Brittish Summer Time)
        current_time_bst = datetime.now(tz).strftime('%H:%M')
        current_day_bst = datetime.now(tz).strftime('%A')
        current_date_bst = datetime.now(tz).strftime('%Y-%m-%d')


        cnx=mysql.connector.connect(
            host='occupancy-db.craysy60cdwy.us-east-2.rds.amazonaws.com',
            user='admin',
            password='shu8Ren8',
            database='occupancy_schema'
        )

        cursor = cnx.cursor()

        insert_query = """
        INSERT INTO occupancy_data (
            percentage_column, bst_time, day_of_week, current_date_bst, temperature, humidity, chance_of_rain, wind
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Values to insert
        values = (occupancy_number, current_time_bst, current_day_bst, current_date_bst, temp_text, humidity_text, rain_text, wind_text)
        
        
        cursor.execute(insert_query, values)

        # Commit the transaction
        cnx.commit()

        cursor.close()
        cnx.close()

        # Get the results
        driver.quit()
        # return {
        #     'statusCode': 200,
        #     'testMessage':'test',
        #     'body': percentage
        # }
    finally:
        if driver:
            driver.quit()
        # if cnx:
        #     cnx.close()