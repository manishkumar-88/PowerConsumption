# PowerConsumption
## Flask RESTful API for Power Consumption Data
This Flask application provides a RESTful API for querying power consumption data. It allows users to retrieve time-series data and filter it based on various criteria such as value, start time, and end time. The timeseries data is from 2008-01-01 to 2008-01-31

## Features
Get Time Slots: Retrieve time slots from the time-series data that fulfill the provided criteria (e.g., value is zero). Users can specify a start and end timestamp to retrieve data within that range.
## Installation
Clone the repository:
`git clone https://github.com/manishkumar-88/PowerConsumption.git`

Make sure you have Python installed on your system.

Navigate to the project directory:
`cd power-consumption-api`

Install dependencies:
`pip install -r requirements.txt`

Set up the MongoDB database by updating the connection URI in app.config.(default connect to localhost.)</br>

## Usage
Start the Flask application:
`python app.py`
Use the following endpoints to interact with the API:

GET api/v1/data: Retrieve time slots based on provided criteria.

Parameters -

`value`: Criterion for filtering the data (default is zero).<br/>
`startTime`: Start timestamp for the filter range (format: YYYY-MM-DDTHH:MM:SS).<br/>
`endTime`: End timestamp for the filter range (format: YYYY-MM-DDTHH:MM:SS).

Response -

A JSON array of objects representing time slots that fulfill the criteria. Each object contains the following fields:<br/>
**start**: Start timestamp of the time slot.
**end**: End timestamp of the time slot.
**duration**: Duration of the time slot in minutes.

`Example:` api/v1/data?value=5&startTime=2008-01-01T05:00:00&endTime=2008-01-25T08:00:00

![image](https://github.com/manishkumar-88/PowerConsumption/assets/96113822/bc51ba84-e772-4afa-8a53-e9e76291ede2)




### Loading Data into MongoDB
To load data from a CSV file into MongoDB, follow these steps
Navigate to the scripts directory:

`cd scripts`

#### Install dependencies:
`pip install -r requirements.txt`

Run the load_data_into_mongodb.py script:
`python load_data_into_mongodb.py`

This script connects to MongoDB, reads data from the specified CSV file, and inserts it into the MongoDB database.

Script Details
The load_data_into_mongodb.py script performs the following actions:
This CSV file contains house hold power consumption data from 2008-01-01 to 2008-01-31 for a regular 1 minute interval of time.
To make the read and usage easy, I have changed one filed name to **value** in csv file .

Connects to MongoDB using pymongo.
Reads data from the specified CSV file into a pandas DataFrame.
Transforms the data if necessary.
Inserts all rows of data into the MongoDB collection .
This perform Atomic Insertion means either all data will be saved to db or none.
Configuration
Make sure to configure the MongoDB connection string and other parameters in the script according to your setup.


## Testing
To run the unit tests, execute the following command:

`python -m unittest .\tests\test_power_onsumption.py`

