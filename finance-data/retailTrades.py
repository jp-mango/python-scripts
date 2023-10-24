import requests
import os
import datetime
import pandas as pd
import configparser

# Loading configuration from the config.ini file using its absolute path
config = configparser.ConfigParser()
config.read(os.path.abspath('C:/Users/menzi/Code/NQ Tables/retail-activity/retailTrades.ini'))
api_key = config.get('API', 'api_key')

# Format: https://data.nasdaq.com/api/v3/datatables/{Table Code}/.{csv,json,xml}?api_key={api}
table_url = f'https://data.nasdaq.com/api/v3/datatables/NDAQ/RTAT10.csv?api_key={api_key}'
output_folder = 'C:/Users/menzi/Code/NQ Tables/retail-activity'
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

        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# table name
download_and_save_csv(table_url, "RTAT10")

def send_to_discord_with_files(webhook_url, content, file_paths):
    files = {}
    open_files = []  # List to keep track of open file handles
    temp_files = []  # List to store paths of temporary files (for cleanup later)

    for index, file_path in enumerate(file_paths):
        # Extract first 11 rows and save to a new file
        df = pd.read_csv(file_path)
        df_head = df.head(10)
        temp_file_path = os.path.join(output_folder, f"temp_{os.path.basename(file_path)}")
        df_head.to_csv(temp_file_path, index=False)
        temp_files.append(temp_file_path)  # Store path for cleanup

        file = open(temp_file_path, 'rb')
        open_files.append(file)  # Store the file handle
        file_key = f"file{index}"  # 'file0', 'file1', etc.
        files[file_key] = (os.path.basename(temp_file_path), file)

    data = {"content": content}
    response = requests.post(webhook_url, data=data, files=files)

    # Close all open files and remove temporary files
    for file in open_files:
        file.close()
    for temp_file in temp_files:
        os.remove(temp_file)

    if response.status_code != 204:  # 204 is the expected successful response code from Discord for a webhook post
        print(f"Failed to send files to Discord. Response Code: {response.status_code}. Response: {response.text}")


# Discord webhook info:
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
while yesterday.weekday() > 4:  # 0 = Monday, 1 = Tuesday, ... , 6 = Sunday
    yesterday -= datetime.timedelta(days=1)

yesterday_date = yesterday.strftime('%m/%d/%Y')
webhook_url = config.get('DISCORD', 'webhook_url')
message = f"Here's updated __**retail trader activity & sentiment**__ for {yesterday_date}!"

# Get all .csv files in the directory
all_files = os.listdir(output_folder)
csv_files = [os.path.join(output_folder, file) for file in all_files if file.endswith('.csv')]

send_to_discord_with_files(webhook_url, message, csv_files)