*Environment
*** This project utelizes a python virtual environment:

`source myenv/bin/activate`

*** To exit:

`deactivate`

* Run The Scraping Program 

*** To run the program once:
`python src/scraping/extractOccupancy.py`
Results saved to sqlite database in /occupancy_data/gym_occupancy_data.db

*** To run a script to keep the program running for 12 hours:
`python src/scraping/twelve_hour_data_collection.py`


* Predicting Future Occupancy
** Preparing TensorFlow model
*** Convert the sql into a dataframe, data cleaned for tensorflow in the process
`python src/predicting/convertingtodf`

*** To generate the ML model:
Including specific date in model features (Inconsistent results due to so far insufficient data) 
`python src/predicting/generatePredictiveModel`

Not including specific date in model features (Reccomended)
`python src/predicting/generateModelNoDay`

** Predicting using TensorFlow Model
To generate prediction on a dataset with day (Not Reccomended)
`python src/predicting/makePrediction`
To generate prediction on a dataset with no day (Reccomended)
`python src/predicting/makePredictionNoDay`




