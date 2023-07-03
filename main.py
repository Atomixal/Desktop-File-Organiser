import os
import shutil

# Takes the input for the file path
DriveName = input("Enter the name of your drive e.g. 'C': ")
Name = os.environ.get("USERNAME", input("Enter your windows username: "))
Directory = input("Enter the directory you want to clean e.g. 'Desktop': ")

def organize_files(directory):
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue
        # Get the file extension
        file_ext = filename.split('.')[-1]
        # Handle files with no extensions
        if file_ext == filename:
            file_ext = 'no_extension'
        # Create a new directory for the file extension if it doesn't exist
        ext_dir = os.path.join(directory, file_ext)
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)
        # Move the file to the new directory
        file_path = os.path.join(directory, filename)
        new_path = os.path.join(ext_dir, filename)
        shutil.move(file_path, new_path)

file_path = (f'{DriveName}:/Users/{Name}/{Directory}')
# Runs the function
organize_files(file_path)
# Notifies the user it is done
input("Done!")
