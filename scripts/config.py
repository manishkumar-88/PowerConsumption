class Settings:
    """
    Class to hold configuration parameters
    """
    DATABASE_HOST = "mongodb://localhost:27017"
    DATABASE_NAME = "PowerConsumption"
    COLLECTION_NAME = "timeseries"
    TIME_FIELD ='ts'
    FILENAME ='household_power_consumption.csv'