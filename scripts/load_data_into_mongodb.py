import pandas as pd
from pymongo import MongoClient
from config import Settings

def insert_to_mongo(data):
    print('Connecting to Mongo database')
    collection_name = Settings.COLLECTION_NAME
    client = MongoClient(Settings.DATABASE_HOST)
    db = client[Settings.DATABASE_NAME]  
    collection = db[collection_name]  

    # check if collection exists 
    if collection_name in db.list_collection_names():
        print(f"Collection {collection_name} already exists. Skipping creation.")   
    else:  
        #options for create the time-series collection
        options = {
            'timeseries': {
                'timeField': Settings.TIME_FIELD,
            }}
        db.create_collection(collection_name, **options)
        print(f"Collection {collection_name} created.")
    
    res = collection.insert_many(data)
    if len(res.inserted_ids)>0:
        print("Data inserted into MongoDB collection.")


if __name__ == "__main__":
    print('Reading CSV and converting data into list of dictionaries...')
    df = pd.read_csv(Settings.FILENAME)
    df['ts'] = pd.to_datetime(df['Date'] + ' ' + df['Time'],dayfirst=True) # date time column into ts
    df.drop(columns=['Date', 'Time'],axis=1, inplace=True) 
    data = df.to_dict(orient='records')
    insert_to_mongo(data)

