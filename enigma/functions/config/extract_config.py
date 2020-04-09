"""Module to deconstruct config into individual variables"""


def extract_config(config):
    """Function to deconstruct config into individual variables"""

    # Extract the switchboard pairs
    switchboard_pairs = config["switchboard_pairs"]

    # Extract the left rotor
    left_rotor = config["left_rotor"]

    left_rotor_id = left_rotor["id"]
    left_rotor_initial_letter = left_rotor["initial_letter"]

    # Extract the middle rotor
    middle_rotor = config["middle_rotor"]

    middle_rotor_id = middle_rotor["id"]
    middle_rotor_initial_letter = middle_rotor["initial_letter"]

    # Extract the right rotor
    right_rotor = config["right_rotor"]

    right_rotor_id = right_rotor["id"]
    right_rotor_initial_letter = right_rotor["initial_letter"]

    # Extract the reflector
    reflector = config["reflector"]

    reflector_id = reflector["id"]

    return \
        switchboard_pairs, \
        left_rotor_id, \
        left_rotor_initial_letter, \
        middle_rotor_id, \
        middle_rotor_initial_letter, \
        right_rotor_id, \
        right_rotor_initial_letter, \
        reflector_id


if __name__ == "__main__":

    from enigma.functions.config.default_config import config

    print(config)

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

    print(switchboard_pairs)
    print(left_rotor_id)
    print(left_rotor_initial_letter)
    print(middle_rotor_id)
    print(middle_rotor_initial_letter)
    print(right_rotor_id)
    print(right_rotor_initial_letter)
    print(reflector_id)
