# import os
# from bs4 import BeautifulSoup

# # Path to the main directory containing the genome folders
# main_directory = 'path/to/your/genomes'

# # Dictionary to hold the genome accession numbers and their corresponding BCG counts
# bcg_counts = {}

# # Iterate over each folder in the main directory
# for folder in os.listdir(main_directory):
#     folder_path = os.path.join(main_directory, folder)
    
#     # Check if it is a directory
#     if os.path.isdir(folder_path):
#         # Look for the index.html file in the folder
#         index_file_path = os.path.join(folder_path, 'index.html')
        
#         if os.path.exists(index_file_path):
#             with open(index_file_path, 'r') as file:
#                 soup = BeautifulSoup(file, 'html.parser')

#                 # Find the element that contains the BCG count
#                 # Adjust the selector based on the HTML structure
#                 bcg_count_element = soup.find('span', class_='bcg-count')  # Change this as needed
#                 if bcg_count_element:
#                     count = int(bcg_count_element.text.strip())
#                     # Store the count with the folder name as the genome accession number
#                     bcg_counts[folder] = count

# # Print the BCG counts
# for genome, count in bcg_counts.items():
#     print(f"{genome}: {count} BCGs")


# excel_file = 'F:/corynebacterium_glutamicum/cynobacterium_antismash.xlsx'
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the Excel file
excel_file = 'F:/corynebacterium_glutamicum/cynobacterium_antismash.xlsx'
df = pd.read_excel(excel_file)

# Print the column names to check
print(df.columns)

# Initialize a list to store results
results = []

# Define the anchors to check
anchors = ['r1c1', 'r1c2', 'r1c3', 'r1c4']

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    accession_number = row['Accession Number']  
    base_url = row['URL']  # Assuming this contains the base URL

    total_count = 0
    found_count = False

    # Iterate over the defined anchors
    for anchor in anchors:
        # Construct the full URL with the anchor
        url_with_anchor = f"{base_url}#{anchor}"
        print(f"Fetching URL: {url_with_anchor}")  # Debugging line
        
        try:
            # Fetch the HTML content from the URL
            response = requests.get(url_with_anchor)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the element that contains the BCG count
            # Update the classes based on your HTML structure
            bcg_count_element = soup.find('span', class_=['legend-type-biosynthetic-additional', 'legend-type-biosynthetic'])
            
            if bcg_count_element:
                count = int(bcg_count_element.text.strip())
                total_count += count
                found_count = True
                print(f"Found count for {accession_number} at {url_with_anchor}: {count}")  # Debugging line
            
        except Exception as e:
            print(f"Error processing {accession_number} at {url_with_anchor}: {e}")

    # If no count was found, set count to 0
    if not found_count:
        total_count = 0

    # Append the result
    results.append({'Accession Number': accession_number, 'Total BCG Count': total_count})

# Convert results to DataFrame for easy output
results_df = pd.DataFrame(results)

# Print the results
print(results_df)

# Optionally save the results to a new Excel file
results_df.to_excel('F:/corynebacterium_glutamicum/bcg_counts.xlsx', index=False)

