import os
import shutil

DEST = r"C:\AppData-Noteside"
os.makedirs(DEST, exist_ok=True)
cwd = os.getcwd()

folders_to_move = ["Notes", "Dict", "data"]

for folder in folders_to_move:
    src_folder = os.path.join(cwd, folder)
    dest_folder = os.path.join(DEST, folder)
    if os.path.exists(src_folder):
        os.makedirs(dest_folder, exist_ok=True)  # make sure destination exists
        # move all contents inside the folder
        for item in os.listdir(src_folder):
            shutil.move(os.path.join(src_folder, item), dest_folder)
        # optionally remove the now-empty source folder
        os.rmdir(src_folder)

print("Noteside installer move complete.")

