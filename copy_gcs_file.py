#copy_gcs_file.py
import os
import shutil

source_directory = "/Users/khandker_shahed/Documents/vibrio_anguillarum/gcs_files/ncbi_dataset/ncbi_dataset/data"

# Define the destination directory where you want to copy and rename the files
destination_directory = "/Users/khandker_shahed/Documents/vibrio_anguillarum/gcs_files/"

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
        # Construct the path to the 'cds_from_genomic.fna' file in the current folder
        source_file = os.path.join(folder_path, 'cds_from_genomic.fna')
        
        # Check if the file exists in the folder
        if os.path.exists(source_file):
            # Define the new file name using the folder (GenBank assembly) name
            new_file_name = f"{folder_name}.fna"
            destination_file = os.path.join(destination_directory, new_file_name)
            
            # Copy and rename the file to the destination directory
            shutil.copy2(source_file, destination_file)
            copied_files.append(folder_name)
            print(f"Copied and renamed: {source_file} to {destination_file}")
        else:
            missing_files.append(folder_name)
            print(f"File not found in folder: {folder_name}")

# Summary of the operation
print("\nSummary:")
print(f"Total files copied: {len(copied_files)}")
print(f"Total files missing: {len(missing_files)}")

if missing_files:
    print("Folders missing the 'cds_from_genomic.fna' file:")
    for folder in missing_files:
        print(f"- {folder}")


