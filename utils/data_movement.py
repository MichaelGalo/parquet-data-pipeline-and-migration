import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

load_dotenv()

neon_connection_string = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOSTNAME')}/neondb?sslmode=require"
engine = create_engine(neon_connection_string)
local_session = sessionmaker(bind=engine)


def upload_data_to_neon(dataframe):
    try:
        dataframe.to_sql("my_table", con=engine, index=False)
    except Exception as e:
        print(f"An error occurred while uploading data to Neon: {e}")


def download_data_from_neon(table):
    session = local_session()
    try:
        result = session.execute(select(table))
        rows = result.fetchall()
        return rows
    except Exception as e:
        print(f"An error occurred while downloading data from Neon: {e}")
    finally:
        session.close()


def upload_data_to_mongo(data):
    pass
