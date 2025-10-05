import pandas as pd
from sqlalchemy import create_engine
from utils import SCHEMA
from logger import logger


class DataIngestion:
    def __init__(self, db_params):
        self.db_params = db_params
        

    def ingest_csv_data(self, csv_file, table_name):
        logger.info(f"🚀 Starting ingestion for file: {csv_file} into table {SCHEMA}.{table_name}")
        try:
            df = pd.read_csv(csv_file, encoding='latin1')
            
            
            engine = create_engine(f'postgresql+psycopg2://{self.db_params["user"]}:{self.db_params["password"]}@{self.db_params["host"]}:{self.db_params["port"]}/{self.db_params["dbname"]}')

            df.to_sql(table_name, engine, schema=SCHEMA, if_exists='replace', index=False)

            logger.info(f"✅ Successfully ingested {len(df)} rows into {SCHEMA}.\"{table_name}\"")
        except Exception as e:
            logger.error(f"❌ Failed during CSV ingestion: {e}")
            raise

    