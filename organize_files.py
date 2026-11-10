
import os
import shutil

# Get the main project folder
main_folder = os.path.dirname(os.path.abspath(__file__))

# List of files to move
files = [
    "app.py",
    "data_cleaning.py",
    "eda.py",
    "requirements.txt"
]

# Move files from data folder to main folder
for file in files:

    old_path = os.path.join(main_folder, "data", file)
    new_path = os.path.join(main_folder, file)

    if os.path.exists(old_path):

        if not os.path.exists(new_path):
            shutil.move(old_path, new_path)
            print(file, "moved successfully!")

        else:
            print(file, "already exists in main folder.")

    else:
        print(file, "not found inside data folder.")

print("\nProject files organized successfully!")
