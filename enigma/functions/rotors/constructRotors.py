"""Module for constructing rotors"""

from enigma.functions.rotors.defineRotors import interface, switchboard, rotorDict, reflectorDict


def constructInterface():
    """Function to construct the enigma interface"""

    # Build the interface
    interface.build()

    return interface


def constructSwitchboard():
    """Function to construct the switchboard"""

    # Build the switchboard
    switchboard.build()

    return switchboard


def constructRotorFromId(rotorId):
    """Function to construct a given rotor"""

    # Get the config for the requested rotor
    try:

        rotor = rotorDict[rotorId]

    except KeyError:

        raise ValueError("Invalid rotor id")

    # Build the rotor
    rotor.build()

    return rotor


def constructReflectorFromId(reflectorId):
    """Function to construct a given reflector"""

    # Get the config for the requested reflector
    try:

        reflector = reflectorDict[reflectorId]

    except KeyError:

        raise ValueError("Invalid reflector id")

    # Build the reflector
    reflector.build()

    return reflector


def constructRotors(leftRotorId, middleRotorId, rightRotorId, reflectorId):
    """Function for constructing a given set of rotors"""

    # Build the interface rotor
    interface = constructInterface()

    # Build the switchboard
    switchboard = constructSwitchboard()

    # Build all requested rotors
    leftRotor = constructRotorFromId(leftRotorId)
    middleRotor = constructRotorFromId(middleRotorId)
    rightRotor = constructRotorFromId(rightRotorId)

    # Set the rotor periods of rotation
    leftRotor.setPeriodOfRotation(1)
    middleRotor.setPeriodOfRotation(12)
    rightRotor.setPeriodOfRotation(26)

    # Build the requested reflector
    reflector = constructReflectorFromId(reflectorId)

    return interface, switchboard, leftRotor, middleRotor, rightRotor, reflector


if __name__ == "__main__":

    #print(constructRotorFromId(2))

    (
        interface,
        switchboard,
        leftRotor,
        middleRotor,
        rightRotor,
        reflector
    ) = constructRotors(
        reflectorId=1,
        leftRotorId=2,
        middleRotorId=3,
        rightRotorId=4
    )

    print(interface.data)
    print(switchboard.data)
    print(leftRotor.data)
    print(middleRotor.data)
    print(rightRotor.data)
    print(reflector.data)
