import time
from datetime import datetime, timedelta
from scraping.main import main 

# Set the duration for 12 hours
duration = timedelta(hours=12)
end_time = datetime.now() + duration

print('beggining the twelve hour data colleciton')

while datetime.now() < end_time:
    main()  # Call imported extractOccupancy function
    time.sleep(300)  # Wait for 5 minutes (300 seconds)

print('finished 12 hour data collection')