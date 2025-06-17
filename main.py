import os
from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine

load_dotenv()

# Connection to Neon
neon_connection_string = f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOSTNAME')}/neondb?sslmode=require"
engine = create_engine(neon_connection_string)
connection = engine.connect()

# Connect to MongoDB
mongo_connection_string = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOSTNAME')}/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_connection_string)
mongo_database = "Lab_One_10"
db = mongo_client[mongo_database]

# Either SQLAlchemy DB reflection or Table creation for .parquet data


# logic for data movement
def upload_data_to_neon(data):
    pass


def download_data_from_neon():
    pass


def upload_data_to_mongo(data):
    pass


def validate_mongo_connection():
    try:
        mongo_client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def main():
    validate_mongo_connection()


if __name__ == "__main__":
    main()
