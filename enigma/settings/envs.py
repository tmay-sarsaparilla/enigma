"""Module for defining defaults"""

# Specify default config
switchboard_pairs = [

    ("B", "J"),
    ("K", "D"),
    ("A", "P"),
    ("Q", "F"),
    ("T", "S")

]

left_rotor = {

    "id": 1,
    "initial_letter": "G"

}

middle_rotor = {

    "id": 2,
    "initial_letter": "O"

}

right_rotor = {

    "id": 3,
    "initial_letter": "W"

}

reflector = {

    "id": 1

}

default_config = {

    "left_rotor": left_rotor,
    "middle_rotor": middle_rotor,
    "right_rotor": right_rotor,
    "reflector": reflector,
    "switchboard_pairs": switchboard_pairs

}
