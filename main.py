import os
from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine, Table, MetaData
from utils import (
    validate_mongo_connection,
    validate_neon_connection,
    upload_data_to_neon,
    download_data_from_neon,
)
import pandas as pd

load_dotenv()

# Connection to Neon & MetaData Details
neon_connection_string = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOSTNAME')}/neondb?sslmode=require"
engine = create_engine(neon_connection_string)
connection = engine.connect()
metadata = MetaData()
postgres_cars = Table("my_table", metadata, autoload_with=engine)

# Connect to MongoDB
mongo_connection_string = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOSTNAME')}/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_connection_string)
mongo_database = "Lab_One_10"
db = mongo_client[mongo_database]


def parse_parquet(file):
    df = pd.read_parquet(file)
    return df


def main():
    # Validate DB Connections
    # validate_mongo_connection()
    # validate_neon_connection(engine)

    # Transform Data for Storage
    # parsed_parquet_dataframe = parse_parquet("data/mtcars.parquet")

    # Upload to Postgres
    # upload_data_to_neon(parsed_parquet_dataframe)

    # Ingest from Postgres
    neon_data = download_data_from_neon(postgres_cars)

    # Upload to MongoDB -- FIXME this expects a list of dictionaries and throws error. Need to transfer to SQLalchemy objects into a python dictionary
    db.cars.insert_many(neon_data)

    # Download from Mongo -- #TODO


if __name__ == "__main__":
    main()
