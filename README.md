The scraping aspect of this project is now also done using Amazon Web Services Lambda, EventBridge, and RDS DB. This is achieved through uploading a containerized version of the code base to AWS Lambda, and then running it while the target gym is open every 20 minutes using EventBridge. It then uploads to a corresponding MySQL database in Python. 

The majority of the data for this project is now taken from the AWS hosted DB, which contains much more data over a longer period and also contains more recent data. However, the local SQLite DB is still useful for testing and local runs of the program, and as a result, is still used occasionally.

To run the local version of the project, follow the steps for scraping below. The process of creating a predictive model using Tensorflow is also done locally (to save hosting costs which would come from running through AWS). As a result, the instructions are the same once the data is collected from the corresponding DB and converted into a Numpy DataFrame. There are corresponding scripts to collect data from the local DB, or the AWS hosted DB, and is explained further below. 


# Setting up local Python virtual environment
### This project utilizes a Python virtual environment:

`source myenv/bin/activate`

### To exit:

`deactivate`

# Run The Scraping Program in virtual environment

### To run the program once:
`python src/scraping/extractOccupancy.py`
Results saved to sqlite database in /occupancy_data/gym_occupancy_data.db

### To run a script to keep the program running for 12 hours:
`python src/scraping/twelve_hour_data_collection.py`


# Predicting Future Occupancy
## Preparing TensorFlow model
### Convert the SQL into a data frame, data cleaned for TensorFlow in the process
When converting locally stored SQLite DB
`python src/predicting/convertingtodf`
When converting AWS hosted RDS MYSQL DB 
`python src/predicting/convertingAWStodf`

### To generate the ML model:
Including specific date in model features (Inconsistent results due to so far insufficient data) 
`python src/predicting/generatePredictiveModel`

Not including specific date in model features (Recommended)
`python src/predicting/generateModelNoDay`

## Predicting using TensorFlow Model
To generate prediction on a dataset with day (Not Recommended)
`python src/predicting/makePrediction`
To generate prediction on a dataset with no day (Recommended)
`python src/predicting/makePredictionNoDay`


# Example Full Program Run (assuming existing database)
`python src/predicting/convertingtodf`

`python src/predicting/generateModelNoDay`

`python src/predicting/makePredictionNoDay`




