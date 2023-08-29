import pandas as pd

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/FIFA_World_Cup'

# Read HTML tables from the URL
tables = pd.read_html(url)

# change value for how many tables down
table_df = tables[3]

# Print the DataFrame
print(table_df)

# Export the DataFrame to a CSV file
filename = 'table_data.csv'
table_df.to_csv(filename, index=False)

print(f"Table saved as: {filename}")
