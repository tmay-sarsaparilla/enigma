"""Module for constructing rotors"""

from enigma.functions.rotors.define_rotors import interface, switchboard, rotor_dict, reflector_dict
from enigma.functions.config.extract_config import extract_config


def construct_interface():
    """Function to construct the enigma interface"""

    # Build the interface
    interface.build()

    return interface


def construct_switchboard(switchboard_pairs):
    """Function to construct the switchboard"""

    # Set the switchboard pairs
    switchboard.assign_pairs(switchboard_pairs)

    # Build the switchboard
    switchboard.build()

    return switchboard


def construct_rotor_from_id(rotor_id, initial_letter):
    """Function to construct a given rotor"""

    # Get the config for the requested rotor
    try:

        rotor = rotor_dict[rotor_id]

    except KeyError:

        raise ValueError("Invalid rotor id")

    # Set the initial letter
    rotor.set_initial_letter(initial_letter=initial_letter)

    # Build the rotor
    rotor.build()

    return rotor


def construct_reflector_from_id(reflector_id):
    """Function to construct a given reflector"""

    # Get the config for the requested reflector
    try:

        reflector = reflector_dict[reflector_id]

    except KeyError:

        raise ValueError("Invalid reflector id")

    # Build the reflector
    reflector.build()

    return reflector


def construct_rotors(config):
    """Function for constructing a given set of rotors"""

    (
        switchboard_pairs,
        left_rotor_id,
        left_rotor_initial_letter,
        middle_rotor_id,
        middle_rotor_initial_letter,
        right_rotor_id,
        right_rotor_initial_letter,
        reflector_id
    ) = extract_config(config)

    # Build the interface rotor
    interface = construct_interface()

    # Build the switchboard
    switchboard = construct_switchboard(switchboard_pairs=switchboard_pairs)

    # Build all requested rotors
    left_rotor = construct_rotor_from_id(rotor_id=left_rotor_id, initial_letter=left_rotor_initial_letter)
    middle_rotor = construct_rotor_from_id(rotor_id=middle_rotor_id, initial_letter=middle_rotor_initial_letter)
    right_rotor = construct_rotor_from_id(rotor_id=right_rotor_id, initial_letter=right_rotor_initial_letter)

    # Set the rotor periods of rotation
    left_rotor.set_period_of_rotation(1)
    middle_rotor.set_period_of_rotation(12)
    right_rotor.set_period_of_rotation(26)

    # Build the requested reflector
    reflector = construct_reflector_from_id(reflector_id=reflector_id)

    return interface, switchboard, left_rotor, middle_rotor, right_rotor, reflector


if __name__ == "__main__":

    from enigma.functions.config.default_config import config

    (
        interface,
        switchboard,
        left_rotor,
        middle_rotor,
        right_rotor,
        reflector
    ) = construct_rotors(config=config)

    print(config)
    print(interface.data)
    print(switchboard.data)
    print(left_rotor.data)
    print(middle_rotor.data)
    print(right_rotor.data)
    print(reflector.data)
