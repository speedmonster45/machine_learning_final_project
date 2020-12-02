import os, pickle
import pandas as pd
import numpy as np
from pathlib import Path


def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


# data_folder = Path("C:/Users/Nathan Gillespie/PycharmProjects/machine_learning_final_project/Resources/au_images")
# print(data_folder)
# Run the above function and store its results in a variable.
path_names= get_filepaths("C:/Users/Nathan Gillespie/PycharmProjects/machine_learning_final_project/Resources/au_images/")
for columns in path_names:
    print(columns)
# path_names = path_names.transpose()
path = "C:/Users/Nathan Gillespie/PycharmProjects/machine_learning_final_project/projectFiles/path_names.txt"
with open(path, "w") as output:
    for columns in path_names:
        output.write(str(columns)+ '\n')
with open(path,"r") as file:
        replaced_data = file.read()
        replaced_data = replaced_data.replace('\\', '/')

