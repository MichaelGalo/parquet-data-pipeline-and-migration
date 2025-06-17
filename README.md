# parquet-data-pipeline-and-migration

## Project Overview

This project demonstrates an end-to-end data pipeline that:
- Extracts data from a `.parquet` file
- Loads the data into a Neon Postgres database
- Migrates the data from Postgres to MongoDB
- Runs reports and analysis on the data in MongoDB

The goal is to gain hands-on experience with the Parquet file format, as well as practice moving data between different database systems.

## Pipeline Steps

1. **Extract**: Read data from a `.parquet` file using Python.
2. **Load to Postgres**: Insert the data into a Neon-hosted Postgres database using SQLAlchemy or similar tools.
3. **Migrate to MongoDB**: Transfer the data from Postgres to MongoDB, transforming as needed for document storage.
4. **Reporting**: Run queries and generate reports from MongoDB collections.

## Technologies Used
- Python
- pyarrow (for Parquet file handling)
- SQLAlchemy (for Postgres connection)
- Neon Postgres (cloud database)
- pymongo (for MongoDB connection)
- MongoDB (NoSQL database)
- DBVisualizer (to validate data migration)
- dotenv (for secure variables)

## Getting Started

1. Clone this repository and set up a Python virtual environment.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure your environment variables for database connections in a `.env` file.
4. Run the pipeline script:
   ```sh
   python main.py
   ```

## Configuration

- Update the `.env` file with your Neon Postgres and MongoDB connection details.
- Modify `main.py` as needed for your specific data and reporting requirements.

## Project Structure

- `main.py` — Main pipeline script
- `requirements.txt` — Python dependencies
- `data/mtcars.parquet` — Example Parquet data file
- `pipeline.md` — Task breakdown and project planning

## License

This project is for educational purposes and practice. Feel free to use or adapt for your own learning.
