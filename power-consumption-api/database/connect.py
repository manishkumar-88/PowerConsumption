from mongoengine import connect
from configparser import ConfigParser


config_file = 'config/app.config'
config = ConfigParser()
config.read(config_file)
mongodb_host = config['flask']['DATABASE_HOST']
mongodb_name = config['flask']['DATABASE_NAME']
collection = config['flask']['COLLECTION_NAME']
DB_URI = mongodb_host +'/'+mongodb_name

# Connect to MongoDB server using the specified database connection string
def initialize_db():
    try:
        connect(host= DB_URI)
    except Exception as e:
        print(f"error in connecting: {e}")
        return str(e)
    
