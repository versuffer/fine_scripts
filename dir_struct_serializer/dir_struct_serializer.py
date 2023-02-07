import pathlib


def tree_to_dict(initial_dir_path, tree_dict=None):
    """This function serializes directory structure to python dictionary"""

    tree_dict = tree_dict or {}

    dir_name = pathlib.Path(initial_dir_path).name
    tree_dict[dir_name] = []

    try:
        dir_content = pathlib.Path(initial_dir_path).iterdir()

        for file_path in dir_content:

            branch = file_path.name

            if file_path.is_dir():
                branch = tree_to_dict(file_path)

            tree_dict[dir_name].append(branch)

    except PermissionError:
        tree_dict[dir_name].append('PERMISSION DENIED')

    return tree_dict

