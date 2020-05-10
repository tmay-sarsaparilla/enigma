"""Module to configure the elements of the enigma machine"""

from enigma.functions.rotors.define import Rotor, Interface, Switchboard, Reflector

# Define rotors configurations
interface = Interface(0, 0, "A")

switchboard = Switchboard(0, 0, "A")

rotor1 = Rotor(1, 15, "B")
rotor2 = Rotor(2, 203, "Q")
rotor3 = Rotor(3, 2, "J")
rotor4 = Rotor(4, 59, "V")
rotor5 = Rotor(5, 245, "A")

reflector1 = Reflector(1, 13, "C")
reflector2 = Reflector(2, 98, "K")

# Build dictionaries
rotor_dict = {

    1: rotor1,
    2: rotor2,
    3: rotor3,
    4: rotor4,
    5: rotor5

}

reflector_dict = {

    1: reflector1,
    2: reflector2

}
