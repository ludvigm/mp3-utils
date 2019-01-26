import os
import sys
import random
from lib.collect_songs import collect_files

def print_examples(x):
    examples = random.sample(file_names_all, x)
    for i in range(0, x):
        print("old: " + examples[i][:50])
        print("new: " + examples[i][n_chars:(50+n_chars)])

if len(sys.argv) != 3:
    print('provide two args, path and number of characters to cut from filename.')
    sys.exit(0)

target_folder = str(sys.argv[1])
n_chars = int(sys.argv[2])

if not os.path.isdir(target_folder):
    print("First arg should be a folder path.")
    sys.exit(0)

print("Collecting files...")

files, file_names_all, files_full = collect_files(target_folder)            # Files will be an array of objects { dirpath:str, filenames:[]} where each filename in filenames exist in the directory dirpath

print("Collected " + str(len(file_names_all)) + " files in " + str(len(files)) + " folders. Renaming will cause the below changes: (5 random examples)")
print_examples(5)
inp = input("Rename all selected files? (y) (enter 'm' to see full list of changes)")

if str(inp) == "y":
    for item in files:                                  # Iterate objects
        curr_path = item["dir_path"]
        for file_name in item["file_names"]:               # In each object, iterate filenames
            os.rename(os.path.join(curr_path, file_name), os.path.join(curr_path, file_name[n_chars:]))     # Rename file.
    print(str(len(file_names_all)) + " songs renamed, bucko!")
elif str(inp) == "m":
    print_examples(len(file_names_all))            # Print all
else:
    sys.exit(0)
