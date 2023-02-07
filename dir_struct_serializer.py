import os
import re
from pprint import pprint


def tree_to_dict(initial_dir_path, tree_dict=None):

    tree_dict = tree_dict or {}

    dir_name = re.findall('[\\\/]?[^\\\/]+\Z', initial_dir_path)[0]
    tree_dict[dir_name] = []
    dir_content = os.listdir(initial_dir_path)

    for i in dir_content:
        step_down = initial_dir_path + '\\' + i
        if os.path.isdir(step_down):
            tree_dict[dir_name].append(tree_to_dict(step_down, dict()))
        else:
            tree_dict[dir_name].append(i)

    return tree_dict


a = tree_to_dict(os.getcwd())
pprint(a)
