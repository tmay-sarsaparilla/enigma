"""Module for finding config files and directory"""

from re import search
from os import path


def get_path_of_user_config_directory():

    # TODO Get this function to work properly

    dir_path = path.expanduser("~\\enigma_user_configs\\")

    return dir_path


def get_path_from_file_name(file_name, dir_path):
    """Function for getting the file path of a saved config from its name"""

    file_path = dir_path + f"{file_name}.pickle"

    return file_path


if __name__ == "__main__":

    dir_path_test = get_path_of_user_config_directory()

    print(dir_path_test)

    file_path_test = get_path_from_file_name("test", dir_path_test)

    print(file_path_test)
