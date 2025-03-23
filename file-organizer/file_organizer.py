import os
import shutil

# Define the destination folders based on file extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar"],
}

def organize(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)

            moved = False
            for category, extensions in file_types.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(folder_path, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    print(f"Moved: {filename} → {category}/")
                    break

            if not moved:
                print(f"Skipped: {filename}")

# Change this path to the folder you want to organize
folder_to_organize = r"C:/Users/YourName/Downloads"
organize(folder_to_organize)
