"""Module for saving user-defined configs"""

from os import mkdir, path
from pickle import dump, HIGHEST_PROTOCOL
from enigma.functions.config.specify_config import prompt_user_for_input
from enigma.functions.config.find_config import get_path_of_user_config_directory, get_path_from_file_name


def create_user_config_directory(dir_path):
    """Function for creating the user_configs directory"""

    # If the directory already exists, do nothing
    if path.isdir(dir_path):

        return

    # Otherwise create the directory
    else:

        mkdir(dir_path)

    return


def choose_file_name():
    """Function to prompt user to choose a file name"""

    # Ask user to choose a file name
    file_name = prompt_user_for_input(
                                      prompt="\nChoose a name for the config: ",
                                      valid_selections=[],
                                      invalid_selection_message="Invalid name. Please use only letters and numbers"
                                      )

    return file_name.lower()


def save_config(config, file_name):
    """Function for a saving a given config to a file with a given name"""

    # Get the path of the user_configs directory
    dir_path = get_path_of_user_config_directory()

    # Check whether the directory exists and if not, create it
    create_user_config_directory(dir_path=dir_path)

    # Get the file path
    file_path = get_path_from_file_name(file_name=file_name, dir_path=dir_path)

    # Check whether the file already exists
    if path.isfile(file_path):

        # Ask user whether to overwrite, cancel, or use a different file name
        write_file = prompt_user_for_input(
                                           prompt="File with that name already exists. "
                                                  "Overwrite? (Y/N) or choose a different config name (R): ",
                                           valid_selections=["Y", "N", "R"],
                                           invalid_selection_message="Invalid selection. Please select Y, N, or R"
                                           )

        # Check whether use chose to use a different file name
        if write_file == "R":

            new_file_name = choose_file_name()

            save_config(config=config, file_name=new_file_name)

            return

        # If user chose not to overwrite, cancel the save
        if write_file == "N":

            return

    # Otherwise write the file
    with open(file_path, "wb") as handle:

        dump(config, handle, protocol=HIGHEST_PROTOCOL)

    return


if __name__ == "__main__":

    from enigma.functions.config.default_config import default_config

    save_config(default_config, "test")
