import csv
# Read data from the first CSV file
file1_data = set()
with open('file1.csv', 'r') as file1: #change name to match filename
    csv_reader = csv.reader(file1)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        file1_data.add(tuple(row))

# Read data from the second CSV file
file2_data = set()
with open('file2.csv', 'r') as file2: #change name to match filename
    csv_reader = csv.reader(file2)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        file2_data.add(tuple(row))

# Merge the data and remove duplicates
merged_data = file1_data.union(file2_data)

# Read the header from one of the original files
with open('file1.csv', 'r') as file1:
    csv_reader = csv.reader(file1)
    header = next(csv_reader)  # Read the header

# Write the merged and deduplicated data to a new CSV file with the same header
with open('merged_file.csv', 'w', newline='') as merged_file:
    csv_writer = csv.writer(merged_file)
    csv_writer.writerow(header)  # Write the header
    csv_writer.writerows(merged_data)