import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

neon_connection_string = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOSTNAME')}/neondb?sslmode=require"
engine = create_engine(neon_connection_string)


def upload_data_to_neon(dataframe):
    try:
        dataframe.to_sql("my_table", con=engine, index=False)
    except Exception as e:
        print(f"An error occurred while uploading data to Neon: {e}")


def download_data_from_neon():
    pass


def upload_data_to_mongo(data):
    pass
