# import os
# import shutil

# def copy_files_with_extension(source_directory, destination_directory, file_extension):
#     # Ensure the destination directory exists
#     os.makedirs(destination_directory, exist_ok=True)
    
#     # Initialize lists to track copied and missing files
#     copied_files = []
#     missing_files = []

#     # Iterate over each folder in the source directory
#     for folder_name in os.listdir(source_directory):
#         folder_path = os.path.join(source_directory, folder_name)
        
#         # Check if the current item is a directory
#         if os.path.isdir(folder_path):
#             # Construct the path to the file with the specified extension
#             source_file = os.path.join(folder_path, folder_name + file_extension)
            
#             # Check if the file with the specified extension exists
#             if os.path.exists(source_file):
#                 # Define the new file name and path in the destination directory
#                 new_file_name = f"{folder_name}{file_extension}"
#                 destination_file = os.path.join(destination_directory, new_file_name)
                
#                 try:
#                     # Copy and rename the file to the destination directory
#                     shutil.copy2(source_file, destination_file)
#                     copied_files.append(folder_name)
#                     print(f"Copied and renamed: {source_file} to {destination_file}")
#                 except Exception as e:
#                     print(f"Error copying file {source_file} to {destination_file}: {e}")
#             else:
#                 missing_files.append(folder_name)
#                 print(f"File not found in folder: {folder_name}")

#     # Print a summary of the operation
#     print("\nSummary:")
#     print(f"Total files copied: {len(copied_files)}")
#     print(f"Total files missing: {len(missing_files)}")

#     if missing_files:
#         print("Folders missing the file with the specified extension:")
#         for folder in missing_files:
#             print(f"- {folder}")

# if __name__ == "__main__":
#     # Define your source and destination directories
#     source_directory = "/Users/khandker_shahed/Documents/mycobacterium_marinum/genomes/ncbi_dataset/ncbi_dataset/data"
#     destination_directory = "/Users/khandker_shahed/Documents/mycobacterium_marinum/genomes/gca_files/"
    
#     # Define the file extension to be used
#     file_extension = ".fna"  # Change this to any other extension as needed
    
#     # Call the function with the specified parameters
#     copy_files_with_extension(source_directory, destination_directory, file_extension)


import os
import shutil
import sys

def copy_files_with_extension(source_directory, destination_directory, file_name='index.html'):
    os.makedirs(destination_directory, exist_ok=True)
    
    copied_files = []
    missing_files = []

    for folder_name in os.listdir(source_directory):
        folder_path = os.path.join(source_directory, folder_name)
        
        if os.path.isdir(folder_path):
            source_file = os.path.join(folder_path, file_name)

            if os.path.isfile(source_file):
                new_file_name = f"{folder_name}.html"
                destination_file = os.path.join(destination_directory, new_file_name)
                
                try:
                    shutil.copy2(source_file, destination_file)
                    copied_files.append(folder_name)
                    print(f"Copied and renamed: {source_file} to {destination_file}")
                except Exception as e:
                    print(f"Error copying file {source_file} to {destination_file}: {e}")
            else:
                missing_files.append(folder_name)
                print(f"File not found in folder: {folder_name}")

    print("\nSummary:")
    print(f"Total files copied: {len(copied_files)}")
    print(f"Total files missing: {len(missing_files)}")

    if missing_files:
        print("Folders missing the file with the specified name:")
        for folder in missing_files:
            print(f"- {folder}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <source_directory> <destination_directory> <file_name>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    file_name = sys.argv[3]

    copy_files_with_extension(source_directory, destination_directory, file_name)
