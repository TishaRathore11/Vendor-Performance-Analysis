import pandas as pd 
import os
import logging
from sqlalchemy import create_engine
import time
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level = logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a")
#connect python to database(inventory.db) 
engine = create_engine('sqlite:///inventory.db')  

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

def load_raw_data():
    start = time.time()
    #fethcing files in data folder
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file) #loads csv files into pandas dataframe
            logging.info(f'Ingesting {file} in db')
            ingest_db(df,file[:-4],engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('Ingestion Complete')
    logging.info('Total Time Taken: {total_time} minutes')
            
        