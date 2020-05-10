"""Module for prompting users to supply messages to be encrypted"""

from enigma.functions.interface.specify__user_config import prompt_user_for_input
from enigma.settings import default_config
from enigma.functions.encryption import encrypt


def encrypt_with_config(config=default_config):
    """Function for prompting users to supply a message then encrypting with a given config"""

    # Get the user to input a message
    input_message = input("\nEnter the message you want to encrypt (only letters will be encrypted): ")

    # Encrypt the message using the specified config
    output_message = encrypt(input_message=input_message, config=config)

    # Display the encrypted message
    print(f"\nEncrypted message: {output_message}")

    # Ask user if they want to encrypt another message
    continue_choice = prompt_user_for_input(
                                            prompt="Encrypt another message? (Y/N): ",
                                            valid_selections=["Y", "N"],
                                            invalid_selection_message="Invalid selection. Please select Y or N"
                                            )

    # If user wants to continue, run the function again
    if continue_choice == "Y":

        encrypt_with_config(config=config)

    # Otherwise, exit
    else:

        return

    return
