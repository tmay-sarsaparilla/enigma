"""Module for deleting a user config"""

from os import path, remove
from enigma.functions.config.find import get_path_of_user_config_directory, get_path_from_file_name


def delete_config(file_name):
    """Function for deleting a saved config"""

    # Get the path of the user_configs directory
    dir_path = get_path_of_user_config_directory()

    # Get the path of the file to be deleted
    file_path = get_path_from_file_name(file_name=file_name, dir_path=dir_path)

    # Check that the file exists
    if path.exists(file_path):

        # Delete the file
        remove(file_path)

    return
