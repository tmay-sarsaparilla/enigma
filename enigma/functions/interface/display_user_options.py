"""Module for displaying user options"""

from enigma.functions.interface.__init__ import specify_config, \
    save_config, \
    load_config, \
    prompt_user_for_input, \
    get_saved_config_list, \
    choose_file_name


def display_saved_configs(saved_config_list):

    full_option_text = "\nSaved configs:\n"

    for i in range(0, len(saved_config_list)):

        option_text = f"{i + 1}.\t{saved_config_list[i]}\n"

        full_option_text += option_text

    print(full_option_text)

    return


def display_user_options():
    """Function for displaying user options"""

    # Display welcome message and options
    print("Welcome to enigma\n")

    prompt = (
                "1.\tCreate config\n"
                "2.\tUse saved config\n"
                "3.\tUse default config\n"
                "4.\tExit\n\n"
                "Please select an option: "
              )

    # Ask user to choose an option
    option_choice = int(prompt_user_for_input(
                                          prompt=prompt,
                                          valid_selections=["1", "2", "3", "4"],
                                          invalid_selection_message="Invalid selection. "
                                                                    "Please select an option from the list"
                                          ))

    # If create config selected, have user create a config then save it
    if option_choice == 1:

        # Get user to specify config
        user_config = specify_config()

        # Have user choose a file name
        user_file_name = choose_file_name()

        # Save the config to file
        save_config(user_config, user_file_name)

        # Display options again
        display_user_options()

    # If use saved config selected, have user choose a saved config then use it to encrypt
    if option_choice == 2:

        saved_config_list = get_saved_config_list()

        if len(saved_config_list) == 0:

            print("\nThere are no saved configs to load\n")

            display_user_options()

        else:

            # Display saved configs
            display_saved_configs(saved_config_list)

            # Convert to upper case
            valid_config_selections = [i.upper() for i in saved_config_list]

            # Ask user to choose a config
            config_choice = prompt_user_for_input(
                                                  prompt="Select a config from the list: ",
                                                  valid_selections=valid_config_selections,
                                                  invalid_selection_message="Invalid selection. "
                                                                            "Please select a config name from the list"
                                                  )

            chosen_config = load_config(file_name=config_choice)

            print(chosen_config)

    # If use default config selected, use the default config to encrypt
    if option_choice == 3:

        pass

    if option_choice == 4:

        # Print exit message
        print("\nGoodbye")

        return


if __name__ == "__main__":

    display_user_options()
