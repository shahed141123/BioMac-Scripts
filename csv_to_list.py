import csv

# Specify your input CSV file and output .list file
input_csv_file = '/mnt/f/Research/corynebacterium_glutamicum_old/cynobacterium_pangolin.csv'
output_list_file = '/mnt/f/Research/corynebacterium_glutamicum_old/cynobacterium_pangolin.list'

# Open the CSV file and the .list file
with open(input_csv_file, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open(output_list_file, mode='w', encoding='utf-8') as list_file:
        for row in csv_reader:
            # Join the row elements with a space or a comma, depending on your needs
            list_file.write(' '.join(row) + '\n')  # Change ' ' to ',' if you want comma-separated values

print("Conversion completed. The .list file is created.")
