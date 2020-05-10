"""Module for loading configs from file"""

from pickle import load
from os import listdir, path
from enigma.functions.config.find import get_path_of_user_config_directory, get_path_from_file_name


def get_saved_config_list():
    """Function for getting a list of all saved configs"""

    dir_path = get_path_of_user_config_directory()

    # Check whether the config directory exists
    if not path.isdir(dir_path):

        # If not, return an empty list
        return []

    file_list = listdir(dir_path)

    file_name_list = [i.replace(".pickle", "") for i in file_list]

    return file_name_list


def load_config(file_name):
    """Function for loading saved configs"""

    # Get the path of the user_configs directory
    dir_path = get_path_of_user_config_directory()

    # Get the file path
    file_path = get_path_from_file_name(file_name=file_name, dir_path=dir_path)

    # Load the file
    with open(file_path, "rb") as handle:

        config = load(handle)

    return config


if __name__ == "__main__":

    config_test = load_config("test")

    print(config_test)

    print(get_saved_config_list())
