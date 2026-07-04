import pandas as pd 
import os 
from sqlalchemy import create_engine 
import logging
import time

# 1. FIX: Create the 'logs' directory if it doesn't exist yet
os.makedirs("logs", exist_ok=True)

logging.basicConfig( 
    filename="logs/ingestion_db.log", 
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filemode="a" 
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine): 
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def load_raw_data(): 
    '''this function will load the CSVs as dataframe and ingest into db''' 
    start = time.time() 
    
    # Applying the safer file handling practices
    for file in os.listdir('data'): 
        if file.endswith('.csv'): 
            filepath = os.path.join('data', file)
            df = pd.read_csv(filepath) 
            
            logging.info(f'Ingesting {file} in db') 
            table_name = os.path.splitext(file)[0]
            ingest_db(df, table_name, engine) 
            
    end = time.time() 
    total_time = (end - start) / 60 
    logging.info(' -- Ingestion Complete -- ')
    
    # 2. FIX: Moved this inside the function where total_time is defined
    logging.info(f'Total Time Taken: {total_time:.4f} minutes\n')


# 3. FIX: Corrected the dunder main syntax (needs double underscores)
if __name__ == '__main__': 
    load_raw_data()