import os
import shutil
import requests
import kagglehub
from pathlib import Path
from dotenv import load_dotenv
from ingestion import DataIngestion
from logger import logger
from utils import RAW_DATA_DIR, DATASET_URL


# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# database credentials
db_credentials = {
        "dbname":os.getenv('DATABASE_NAME'),
        "user":os.getenv('DATABASE_USER'),
        "password":os.getenv('DATABASE_PASSWORD'),
        "host":os.getenv('DATABASE_HOST'),
        "port":os.getenv('PORT')
    }

def download_kaggle_dataset(dataset_path:str) -> str:
    """ Download kaggle dataset """
    try:
        response = requests.get(f"https://www.kaggle.com/datasets/{dataset_path}")
        
        if response.status_code == 200:
            downloaded_path = Path(kagglehub.dataset_download(dataset_path))
            logger.info(f"✅ Downloading Raw Dataset...")
            # create raw data directory if not exist
            RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

            for item in downloaded_path.iterdir():
                dest = RAW_DATA_DIR / item.name
                if item.is_dir():
                    shutil.copytree(item, dest, dirs_exist_ok=True)
                else:
                    shutil.copy2(item, dest)

            logger.info(f"✅ Raw Dataset now available in: {RAW_DATA_DIR}")
        else:
            logger.error("❌ Invalid Dataset Path.")
    except Exception as err:
        logger.error(f"❌ Resource not available! {err}")




def main():
    if RAW_DATA_DIR is None:
        # Download Dataset
        download_kaggle_dataset(dataset_path=DATASET_URL)
    else:
        logger.info(f"✅ Raw Dataset is already available in: {RAW_DATA_DIR}")

    # Data Ingestion
    data_ingestion = DataIngestion(db_credentials)

    # Ingest data from CSV file
    csv_file = Path('./datasets/raw/Superstore.csv')
    data_ingestion.ingest_csv_data(csv_file, 'raw_orders')


if "__main__" == __name__:
    main()