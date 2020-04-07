"""Module to encrypt a message"""
from enigma.functions.encryption.encrypt_letter import encrypt_letter
from enigma.functions.rotors.construct_rotors import construct_rotors
from enigma.functions.rotors.reset_rotors import reset_rotors
from string import punctuation, whitespace
from textwrap import wrap


def cleanse_input_message(input_message):
    """Function for cleansing an input message"""

    # Remove punctuation or whitespace
    for i in punctuation + whitespace:

        input_message = input_message.replace(i, "")

    # Make upper case
    input_message = input_message.upper()

    # Check for numbers
    if not input_message.isalpha():

        raise ValueError("Message cannot contain numerals")

    return input_message


def encrypt(input_message, config):
    """Function to encrypt a message using a given configuration of rotors"""

    # Prepare the rotors
    (
        interface,
        switchboard,
        left_rotor,
        middle_rotor,
        right_rotor,
        reflector
    ) = construct_rotors(config=config)

    # Initialise the encrypted message
    encrypted_letters = ""

    # Cleanse the input message
    prepared_message = cleanse_input_message(input_message=input_message)

    message_letters = list(prepared_message)

    # Loop through each letter in the message
    for i in range(0, len(message_letters)):

        # Retrieve the letter and index
        letter = message_letters[i]
        letter_index = i

        # TODO Fix bug in rotor rotation
        print(letter)
        print(letter_index)
        print(left_rotor.rotations)

        # Encrypt the letter
        output_letter = encrypt_letter(
                                      input_letter=letter,
                                      letter_index=letter_index,
                                      interface=interface,
                                      switchboard=switchboard,
                                      reflector=reflector,
                                      left_rotor=left_rotor,
                                      middle_rotor=middle_rotor,
                                      right_rotor=right_rotor
                                      )

        # Add to the encrypted string
        encrypted_letters += output_letter

    # Break the encrypted string into chunks of 5 letters
    encrypted_list = wrap(encrypted_letters, 5)

    # Collapse into single string with spaces between chunks
    encrypted_message = " ".join(encrypted_list)

    # Reset the machine
    reset_rotors(
                 interface=interface,
                 switchboard=switchboard,
                 left_rotor=left_rotor,
                 middle_rotor=middle_rotor,
                 right_rotor=right_rotor,
                 reflector=reflector
                 )

    return encrypted_message


if __name__ == "__main__":

    from enigma.functions.config.default_config import config

    inputMessage = "XLPOZ GNGND JFKO"

    encryptedMessage = encrypt(input_message=inputMessage, config=config)

    print(encryptedMessage)

    unencryptedMessage = encrypt(input_message=encryptedMessage, config=config)

    print(unencryptedMessage)
