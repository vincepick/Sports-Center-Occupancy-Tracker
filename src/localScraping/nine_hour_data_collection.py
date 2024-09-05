import time
from datetime import datetime, timedelta
from scraping.main import main 

# Set the duration for 9 hours
duration = timedelta(hours=9)
end_time = datetime.now() + duration

print('beggining the nine hour data colleciton')

while datetime.now() < end_time:
    main()  # Call your imported function
    time.sleep(300)  # Wait for 5 minutes (300 seconds)

print('finished 9 hour data collection')