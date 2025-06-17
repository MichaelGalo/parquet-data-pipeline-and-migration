import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


mongo_connection_string = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOSTNAME')}/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_connection_string)


def validate_mongo_connection():
    try:
        mongo_client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
