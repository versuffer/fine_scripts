import os
import pathlib
from pprint import pprint


def tree_to_dict(initial_dir_path, tree_dict=None):
    """This function serializes directory structure to python dictionary"""

    tree_dict = tree_dict or {}

    dir_name = pathlib.Path(initial_dir_path).name
    tree_dict[dir_name] = []
    dir_content = os.listdir(initial_dir_path)

    for i in dir_content:
        step_down = pathlib.Path(initial_dir_path).joinpath(i)

        if os.path.isdir(step_down):
            tree_dict[dir_name].append(tree_to_dict(step_down, dict()))
        else:
            tree_dict[dir_name].append(i)

    return tree_dict


a = tree_to_dict(os.getcwd())
pprint(a)
