"""Module for finding config files and directory"""

from re import search
from os import getcwd


def get_path_of_user_config_directory():

    wd = getcwd()

    path_to_remove = search("(?<=enigma\\\).+", wd)

    if path_to_remove is None:

        raise ValueError("No directory match found")

    dir_path = wd.replace(path_to_remove.group(0), "")

    dir_path = dir_path + "user_configs\\"

    return dir_path


def get_path_from_file_name(file_name, dir_path):
    """Function for getting the file path of a saved config from its name"""

    file_path = dir_path + f"{file_name}.pickle"

    return file_path
