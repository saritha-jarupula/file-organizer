"""
File Organizer
--------------
Automatically sorts files in a folder into subfolders
based on their file type (Images, Documents, Videos, etc.)

Author: Jarupula Saritha
"""

import os
import shutil

# Define categories and which extensions belong to each
FILE_CATEGORIES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents":  [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos":     [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio":      [".mp3", ".wav", ".aac", ".flac"],
    "Archives":   [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code":       [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
    "Others":     []
}

def get_category(extension):
    """Return the folder category for a given file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    """Organize all files in the given folder into subfolders."""

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders, only process files
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)

        # Find which category this file belongs to
        category = get_category(extension)

        # Create the category subfolder if it doesn't exist
        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file into the category subfolder
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(file_path, destination_path)

        print(f"  Moved: {filename}  -->  {category}/")
        files_moved += 1

    print(f"\nDone! {files_moved} file(s) organized.")

def main():
    print("===== File Organizer =====")
    folder = input("Enter the folder path to organize (or press Enter for current folder): ").strip()

    if folder == "":
        folder = os.getcwd()

    print(f"\nOrganizing folder: {folder}\n")
    organize_folder(folder)

if __name__ == "__main__":
    main()
