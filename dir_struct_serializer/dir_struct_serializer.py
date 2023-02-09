import pathlib
from pprint import pprint


def tree_to_dict(initial_dir_path, tree_dict=None):
    """This function serializes directory structure to python dictionary"""

    tree_dict = tree_dict or {}

    dir_name = pathlib.Path(initial_dir_path).name
    tree_dict[dir_name] = {'type': 'dir',
                           'children': {}}

    dir_content = pathlib.Path(initial_dir_path).iterdir()

    for file_path in dir_content:

        branch_name = file_path.name
        branch_content = {'type': 'file'}

        try:
            if file_path.is_dir():
                branch_content = tree_to_dict(file_path)
                tree_dict[dir_name]['children'][branch_name] = branch_content[branch_name]
                continue

        except PermissionError:
            branch_content = {'type': 'dir',
                              'access': 'PERMISSION_DENIED'}

        tree_dict[dir_name]['children'][branch_name] = branch_content

    return tree_dict


pprint(tree_to_dict(pathlib.Path.cwd()))
