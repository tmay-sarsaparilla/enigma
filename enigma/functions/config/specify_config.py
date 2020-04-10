"""Module to allow users to specify their own config for the machine"""

import re
from string import ascii_uppercase
from enigma.functions.rotors.rotor_configurations import rotor_dict, reflector_dict


def prompt_user_for_input(prompt, valid_selections, invalid_selection_message):
    """Function for prompting users to input a valid selection"""

    input_value = ""
    valid_input = False

    # Continue the loop until the input is valid
    while not valid_input:

        # Get the input from the user
        input_value = input(prompt).upper().strip()

        # If not valid selections supplied, accept any combination of letters and numbers
        if len(valid_selections) == 0:

            match = re.match("^[A-Za-z0-9]+$", input_value)

            # If input contains no special characters, mark as valid
            if match is not None:

                valid_input = True

            # Otherwise repeat
            else:

                print(invalid_selection_message)

        # Otherwise, check against the list of valid inputs
        else:

            # If input is in the valid_selections list, mark as valid
            if input_value in valid_selections:

                valid_input = True

            # Otherwise repeat
            else:

                print(invalid_selection_message)

    return input_value


def specify_switchboard_pairs():
    """Function for prompting users to specify switchboard pairs"""

    # First ask users to choose how many pairs they want in the switchboard
    valid_switchboard_pair_counts = str(list(range(0, 11)))
    invalid_switchboard_count_selection_message = "Invalid selection. Please select a value between 0 and 10"

    switchboard_pair_count = int(prompt_user_for_input(
        prompt="\nChoose number of letter pairs in the switchboard (max 10): ",
        valid_selections=valid_switchboard_pair_counts,
        invalid_selection_message=invalid_switchboard_count_selection_message
    ))

    letters = list(ascii_uppercase)

    switchboard_pairs = []

    # Loop as many times as requested
    for i in range(0, switchboard_pair_count):

        print(f"\nPair {i + 1}")

        # Get users to pick first letter in the pair
        first_letter = prompt_user_for_input(
            prompt=f"Choose first letter in pair {i + 1}: ",
            valid_selections=letters,
            invalid_selection_message="Invalid selection"
        )

        # Remove first letter from available options
        letters.remove(first_letter)

        # Get users to pick second letter in the pair
        second_letter = prompt_user_for_input(
            prompt=f"Choose second letter in pair {i + 1}: ",
            valid_selections=letters,
            invalid_selection_message="Invalid selection"
        )

        # Remove second letter from available options
        letters.remove(second_letter)

        # Add the pair to the list
        switchboard_pairs.append((first_letter, second_letter))

    return switchboard_pairs


def choose_rotor(valid_selections, position):
    """Function for prompting users to choose a rotor"""

    # Display available rotors
    print(f"\nAvailable rotors: {', '.join(valid_selections)}")

    # Ask user to choose a rotor
    rotor_choice = prompt_user_for_input(
        prompt=f"\nChoose a rotor for the {position} position: ",
        valid_selections=valid_selections,
        invalid_selection_message="Invalid selection. Please choose from the available rotors"
    )

    # Remove rotor from the available list
    valid_selections.remove(rotor_choice)

    # Ask user to choose an starting letter
    initial_letter_choice = prompt_user_for_input(
        prompt=f"Choose a starting letter for the rotor: ",
        valid_selections=ascii_uppercase,
        invalid_selection_message="Invalid selection. Please choose a letter A-Z"
    )

    # Build the rotor dictionary entry
    rotor = {

        "id": int(rotor_choice),
        "initial_letter": initial_letter_choice

    }

    return rotor, valid_selections


def choose_reflector(valid_selections):
    """Function for prompting users to choose a reflector"""

    # Display available rotors
    print(f"\nAvailable reflectors: {', '.join(valid_selections)}")

    # Ask user to choose a rotor
    reflector_choice = prompt_user_for_input(
        prompt=f"Choose a reflector: ",
        valid_selections=valid_selections,
        invalid_selection_message="Invalid selection. Please choose from the available reflectors"
    )

    reflector = {

        "id": int(reflector_choice)

    }

    return reflector


def specify_config():
    """Function for prompting users to specify their own machine config"""

    # Initialise config
    config = {}

    # Get users to choose switchboard pairs
    switchboard_pairs = specify_switchboard_pairs()

    # Add the selected pairs to the config
    config["switchboard_pairs"] = switchboard_pairs

    # Get the lists of available rotors and reflectors
    valid_rotors = [str(i) for i in rotor_dict.keys()]
    valid_reflectors = [str(i) for i in reflector_dict.keys()]

    # Get users to choose a rotor and initial letter for the left position
    left_rotor, valid_rotors = choose_rotor(valid_selections=valid_rotors, position="left")

    # Add the left rotor to the config
    config["left_rotor"] = left_rotor

    # Get users to choose a rotor and initial letter for the middle position
    middle_rotor, valid_rotors = choose_rotor(valid_selections=valid_rotors, position="middle")

    # Add the left rotor to the config
    config["middle_rotor"] = middle_rotor

    # Get users to choose a rotor and initial letter for the right position
    right_rotor, valid_rotors = choose_rotor(valid_selections=valid_rotors, position="right")

    # Add the left rotor to the config
    config["right_rotor"] = right_rotor

    # Get users to choose a reflector
    reflector = choose_reflector(valid_selections=valid_reflectors)

    # Add the reflector to the config
    config["reflector"] = reflector

    return config


if __name__ == "__main__":

    config_test = specify_config()

    print(config_test)
