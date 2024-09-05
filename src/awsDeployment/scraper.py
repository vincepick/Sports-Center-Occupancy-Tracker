import re

# Scraper used to retrieve the occupancy percentage from university website
def scrape_occupancy(driver):
    driver.get('https://sport.wp.st-andrews.ac.uk/')
    occupancy_element = driver.find_element(by='xpath', value='/html/body/main/section[2]/div/div/div[2]/h3[1]')
    occupancy_text = occupancy_element.text

    occupancy_number = 0
    # Uses regex to remove the percent sign before entering into the DB
    percentage = re.search(r'(\d+)%', occupancy_text)
    if percentage:
        occupancy_number = int(percentage.group(1))
    
    return occupancy_number

# Scraper to retrieve different weather statistics from UK weather.com
def scrape_weather(driver):
    driver.get('https://weather.com/en-GB/weather/tenday/l/St+Andrews+Scotland?canonicalCityId=56d2f9aaa0f62e8898b3c962f4d833ef1e869b73de2ad388a77bb57fd885c73a')

    # Paths for each of the weather statistics
    tempPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[1]/span'
    humidityPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[2]/ul/li[1]/div/span[2]'
    rainPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[3]/div[1]/span'
    windPath = '/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/div[2]/details[1]/div/div[1]/div/div[3]/div[2]/span/span[2]'

    # Getting the element at each of the paths
    temp_text = driver.find_element(by='xpath', value=(tempPath)).text
    humidity_text = driver.find_element(by='xpath', value=(humidityPath)).text
    rain_text = driver.find_element(by='xpath', value=(rainPath)).text
    wind_text = driver.find_element(by='xpath', value=(windPath)).text

    return temp_text, humidity_text, rain_text, wind_text
