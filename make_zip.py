import os
import zipfile

# Set the directory containing the files
directory = '/mnt/f/Research/corynebacterium_glutamicum_old/gcf_files/'

# Change to the specified directory
os.chdir(directory)

# Loop through all files in the directory
for filename in os.listdir(directory):
    if os.path.isfile(filename):  # Check if it's a file
        # Create a zip file with the same name as the original file
        zip_filename = f"{os.path.splitext(filename)[0]}.zip"
        
        # Create a ZipFile object
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(filename)  # Add the file to the zip file

print("All files have been zipped individually.")
