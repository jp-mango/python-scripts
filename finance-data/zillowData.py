import requests
import os
import psycopg2
import configparser  # Added to read the configuration file
import datetime

# Loading configuration from the config.ini file using its absolute path
config = configparser.ConfigParser()
config.read(os.path.abspath('./zillow_db/zillowData.ini')) # use full filepath if automating

# Define PostgreSQL database connection parameters from the configuration file, and api_key
db_params = {
    "host": config.get('DATABASE', 'host'),
    "database": config.get('DATABASE', 'database_name'),
    "user": config.get('DATABASE', 'user'),
    "password": config.get('DATABASE', 'password')
}
api_key = config.get('API', 'api_key')  # API key from configuration file

# Define the API endpoints for CSV files, and local save
zillow_data_url = f'https://data.nasdaq.com/api/v3/datatables/ZILLOW/DATA.csv?&api_key={api_key}'
zillow_indicators_url = f'https://data.nasdaq.com/api/v3/datatables/ZILLOW/INDICATORS.csv?&api_key={api_key}'
zillow_regions_url = f'https://data.nasdaq.com/api/v3/datatables/ZILLOW/REGIONS.csv?&api_key={api_key}'
output_folder = "zillow_db" # use full filepath if automating
os.makedirs(output_folder, exist_ok=True)

# Define a function to download and save a CSV file
def download_and_save_csv(url, table_name):
    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Construct the file path to save the CSV
            file_name = f"{table_name}.csv"
            file_path = os.path.join(output_folder, file_name) 

            # Save the CSV content to the file
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded and saved {file_name} to {file_path}")

            # Upload the CSV data to PostgreSQL
            upload_csv_to_postgres(file_path, table_name)

        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Use a context manager for database connection handling
class DatabaseConnection:
    def __enter__(self):
        self.conn = psycopg2.connect(**db_params)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

# upload csv to postgress
def upload_csv_to_postgres(csv_path, table_name):
    try:
        with open(csv_path, 'r') as f:
            cursor = conn.cursor()
            
            # Clear the table before inserting new data
            cursor.execute(f"TRUNCATE TABLE public.{table_name} RESTART IDENTITY CASCADE")
            
            # Use the COPY command to load data from the CSV file into the table
            cursor.copy_expert(f"COPY public.{table_name} FROM stdin CSV HEADER", f)
            
        conn.commit()
        print(f"Uploaded data from {csv_path} to public.{table_name} \n")

    except Exception as e:
        print(f"Error uploading data to public.{table_name}: {str(e)}")
        conn.rollback()  # Rollback the current transaction to prevent it from affecting subsequent uploads

# Wrap the downloading and uploading process in a context manager for the database connection
with DatabaseConnection() as conn:
    download_and_save_csv(zillow_data_url, "zillow_data")
    download_and_save_csv(zillow_indicators_url, "zillow_indicators")
    download_and_save_csv(zillow_regions_url, "zillow_regions")
