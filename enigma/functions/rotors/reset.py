"""Module for resetting rotors to their initial state after encryption is complete"""


def reset_rotors(interface, switchboard, left_rotor, middle_rotor, right_rotor, reflector):
    """Function for resetting all rotors to their initial state"""

    interface.reset()
    switchboard.reset()
    left_rotor.reset()
    middle_rotor.reset()
    right_rotor.reset()
    reflector.reset()

    return
