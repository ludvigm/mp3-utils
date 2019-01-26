import os
import sys
import eyed3
from lib.collect_songs import collect_files

if len(sys.argv) != 3:
    print('provide two args, path and number of characters to cut from filename.')
    sys.exit(0)

folder_from = str(sys.argv[1])
folder_to = str(sys.argv[2])

if not os.path.isdir(folder_from):
    print("First arg should be a folder path.")
    sys.exit(0)

if not os.path.isdir(folder_to):
    print("First arg should be a folder path.")
    sys.exit(0)

#folder_from = "C:/Users/Ludvig/Music/Collection/Beatport Exclusives Only - Week 2 (2019)"
#folder_to = "C:/Users/Ludvig/Music/Collection/sortedtest"

print("Collecting files...")
files, file_names, file_paths = collect_files(folder_from) # Files will be an array of objects { dirpath:str, filenames:[]} where each filename in filenames exist in the directory dirpath
print("Sorting your stuff out")
for i in range(0, len(file_names)):     #range because we need the index for now
    from_file_path = file_paths[i]
    from_file_name = file_names[i]            # array items map 1:1 i.e file_paths[i] will hold the full path to the file file_names[i]

    eyed3file = eyed3.load(from_file_path)
    if(eyed3file):
    #   NOTE: Changing the delimiter will fuck up a song collection that has been sorted using a previous, different delimiter, causing two folders for the same genre.
        if(eyed3file.tag.genre.name):
            genre = eyed3file.tag.genre.name.replace("/", " - ")        # genre.name can containt "/" but paths should not. Using delimiter " - " instead.

            to_dir = os.path.join(folder_to, genre)
            to_path = os.path.join(to_dir, from_file_name)    # New dir, old file name

            if not os.path.isdir(to_dir):
                os.mkdir(to_dir)
                
            try:
                os.rename(from_file_path, to_path)               # move file
            except WindowsError:
                print("File " + from_file_name + " already exists in source! Doing nothing!")    #TODO How to handle this? Delete source file?
        else:
            print("Could not find name of genre tag on file: " + from_file_name)
    else:
        print("Could not load file: " + from_file_name + ". (Probably because the name contains some wierd character)") #TODO Fix handling of funny funny characters such as ' and ñ.
    

print("All done!")