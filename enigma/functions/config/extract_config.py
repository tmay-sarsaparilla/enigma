"""Module to deconstruct config into individual variables"""


def extract_config(config):
    """Function to deconstruct config into individual variables"""

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
        left_rotor_id, \
        left_rotor_initial_letter, \
        middle_rotor_id, \
        middle_rotor_initial_letter, \
        right_rotor_id, \
        right_rotor_initial_letter, \
        reflector_id


if __name__ == "__main__":

    left_rotor = {

        "id": 1,
        "initial_letter": "A"

    }

    middle_rotor = {

        "id": 1,
        "initial_letter": "A"

    }

    right_rotor = {

        "id": 1,
        "initial_letter": "A"

    }

    reflector = {

        "id": 1

    }

    config = {

        "left_rotor": left_rotor,
        "middle_rotor": middle_rotor,
        "right_rotor": right_rotor,
        "reflector": reflector

    }

    print(config)

    (
        left_rotor_id,
        left_rotor_initial_letter,
        middle_rotor_id,
        middle_rotor_initial_letter,
        right_rotor_id,
        right_rotor_initial_letter,
        reflector_id
    ) = extract_config(config)

    print(left_rotor_id)
    print(left_rotor_initial_letter)
    print(middle_rotor_id)
    print(middle_rotor_initial_letter)
    print(right_rotor_id)
    print(right_rotor_initial_letter)
    print(reflector_id)
