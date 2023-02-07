import os
import pathlib
from pprint import pprint


def tree_to_dict(initial_dir_path, tree_dict=None):
    """This function serializes directory structure to python dictionary"""

    tree_dict = tree_dict or {}

    dir_name = pathlib.Path(initial_dir_path).name
    dir_content = os.listdir(initial_dir_path)
    tree_dict[dir_name] = []

    for i in dir_content:

        step_down = pathlib.Path(initial_dir_path).joinpath(i)
        branch = i

        if os.path.isdir(step_down):
            branch = tree_to_dict(step_down, dict())

        tree_dict[dir_name].append(branch)

    return tree_dict


a = pathlib.Path(os.getcwd()).parent.parent
pprint(tree_to_dict(a))

pprint(a)
