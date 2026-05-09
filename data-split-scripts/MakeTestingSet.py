import os
import sys
import shutil

def move_every_fifth(source_folder):
    if not os.path.isdir(source_folder):
        print(f"Error: '{source_folder}' is not a valid directory.")
        return

    # Create destination folder
    dest_folder = os.path.join(source_folder, "test")
    os.makedirs(dest_folder, exist_ok=True)

    # Get sorted list of files only (ignore directories)
    files = os.listdir(source_folder)

    # Move every 5th file (index 4, 9, 14, ...)
    for i, filename in enumerate(files, start=1):
        if i % 5 == 0:
            src_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(dest_folder, filename)

            # print(f"Moving: {filename}")
            shutil.move(src_path, dest_path)

    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python MakeTestingSet.py <folder_path>")
    else:
        move_every_fifth(sys.argv[1])