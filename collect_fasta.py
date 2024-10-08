import os
import shutil

# Define the source directory containing multiple genome folders
# source_directory = "F:/Biosynthetoc gene cluster (Corynebacterium glutamicum)/ncbi_dataset/data"

# # Define the destination directory where you want to copy the files
# destination_directory = "F:/Biosynthetoc gene cluster (Corynebacterium glutamicum)/gcs_files/"

source_directory = 'ncbi_dataset/data'
destination_directory = 'gcf_files'

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Track files that were successfully copied and those that were missing
copied_files = []
missing_files = []

# Iterate over each folder in the source directory
for folder_name in os.listdir(source_directory):
    folder_path = os.path.join(source_directory, folder_name)
    
    # Check if the current item is a folder
    if os.path.isdir(folder_path):
        # Look for all FASTA files in the current folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.fasta') or file_name.endswith('.fa') or file_name.endswith('.fna'):
                # Construct the full path of the source file
                source_file = os.path.join(folder_path, file_name)
                
                # Define the new file name using the folder (GenBank assembly) name
                new_file_name = f"{folder_name}.fna"
                destination_file = os.path.join(destination_directory, new_file_name)
                
                # Copy and rename the file to the destination directory
                shutil.copy2(source_file, destination_file)
                copied_files.append(folder_name)
                print(f"Copied and renamed: {source_file} to {destination_file}")
                break  # Uncomment if you only want the first FASTA file in each folder
        else:
            missing_files.append(folder_name)
            print(f"No FASTA files found in folder: {folder_name}")

# Summary of the operation
print("\nSummary:")
print(f"Total files copied: {len(copied_files)}")
print(f"Total folders missing FASTA files: {len(missing_files)}")

if missing_files:
    print("Folders missing FASTA files:")
    for folder in missing_files:
        print(f"- {folder}")
