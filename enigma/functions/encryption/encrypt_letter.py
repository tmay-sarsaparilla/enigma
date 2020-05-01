"""Module for encrypting a single letter"""


def encrypt_letter(
        input_letter,
        letter_index,
        interface,
        switchboard,
        left_rotor,
        middle_rotor,
        right_rotor,
        reflector
):
    """Function to encrypt a single letter"""

    # The structure of the encryption is thus:
    #   Interface > switchboard > left > middle > right > reflector > right > middle > left > switchboard > interface

    # Apply any necessary rotations
    left_rotor.apply_rotation(letter_index=letter_index)

    middle_rotor.apply_rotation(letter_index=letter_index)

    right_rotor.apply_rotation(letter_index=letter_index)

    # Get the initial input position from the interface
    interface_position = interface.get_position_from_letter(letter=input_letter)

    # Get the switchboard output position
    switchboard_output_position = switchboard.cross_left_to_right(input_position=interface_position)

    # Get the left rotor output position
    left_rotor_output_position = left_rotor.cross_left_to_right(input_position=switchboard_output_position)

    # Get the middle rotor output position
    middle_rotor_output_position = middle_rotor.cross_left_to_right(input_position=left_rotor_output_position)

    # Get the right rotor output position
    right_rotor_output_position = right_rotor.cross_left_to_right(input_position=middle_rotor_output_position)

    # Get the reflector output position
    reflector_output_position = reflector.cross_left_to_right(input_position=right_rotor_output_position)

    # Then we go back the other way

    # Get the right rotor input position
    right_rotor_input_position = right_rotor.cross_right_to_left(output_position=reflector_output_position)

    # Get the middle rotor input position
    middle_rotor_input_position = middle_rotor.cross_right_to_left(output_position=right_rotor_input_position)

    # Get the left rotor input position
    left_rotor_input_position = left_rotor.cross_right_to_left(output_position=middle_rotor_input_position)

    # Get the switchboard input position
    switchboard_input_position = switchboard.cross_right_to_left(output_position=left_rotor_input_position)

    # Get the interface output position
    interface_output_position = interface.cross_right_to_left(output_position=switchboard_input_position)

    # Get the output letter

    output_letter = interface.get_letter_from_position(position=interface_output_position)

    return output_letter


if __name__ == "__main__":

    from enigma.functions.config.default_config import default_config
    from enigma.functions.rotors.construct_rotors import construct_rotors

    (
        interface,
        switchboard,
        leftRotor,
        middleRotor,
        rightRotor,
        reflector
    ) = construct_rotors(config=default_config)

    inputLetter = "A"
    letterIndex = 0

    outputLetter = encrypt_letter(
        input_letter=inputLetter,
        letter_index=letterIndex,
        interface=interface,
        switchboard=switchboard,
        reflector=reflector,
        left_rotor=leftRotor,
        middle_rotor=middleRotor,
        right_rotor=rightRotor
    )

    print(outputLetter)
