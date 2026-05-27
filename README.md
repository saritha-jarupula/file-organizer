# File Organizer 📁

A Python script that automatically sorts files in any folder into subfolders based on file type.

## Features
- Sorts files into: Images, Documents, Videos, Audio, Archives, Code, Others
- Works on any folder you specify
- Simple to run — no extra libraries needed

## How to Run

```bash
python file_organizer.py
```

Then enter the folder path you want to organize, or press Enter to organize the current folder.

## Example Output

```
===== File Organizer =====
Enter the folder path to organize: C:/Users/Saritha/Downloads

Organizing folder: C:/Users/Saritha/Downloads

  Moved: photo.jpg        -->  Images/
  Moved: resume.pdf       -->  Documents/
  Moved: song.mp3         -->  Audio/
  Moved: project.zip      -->  Archives/

Done! 4 file(s) organized.
```

## Technologies Used
- Python 3
- `os` module — folder and file handling
- `shutil` module — moving files

## Author
Jarupula Saritha
