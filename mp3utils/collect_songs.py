import os
from os import walk

def collect_files(root):
    dir_w_files = []              # Will be an array of objects on form { dirpath:str, filenames:[]} where each filename in filenames exist in the directory dirpath
    file_names = []
    file_paths = []

    for (dirpath, dirnames, filenames) in walk(root):
        #lst =      # Collect full paths to files for name-changing later.
        x = {
            "dir_path": dirpath,
            "file_names": filenames
            }
        dir_w_files.append(x)               ## { dirpath:str, filenames:[]}, combine dir path with a filename for full path
        file_names.extend(filenames)        ## All filenames (no dir)
        file_paths.extend(map(lambda x: os.path.join(dirpath, x), filenames))

    return dir_w_files, file_names, file_paths