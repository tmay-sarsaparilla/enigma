"""Module for encrypting a single letter"""
from enigma.functions.encryption.__init__ import *


def encryptLetter(
        inputLetter,
        letterIndex,
        interface,
        leftRotor,
        middleRotor,
        rightRotor,
        reflector
):
    """Function to encrypt a single letter"""

    # The structure of the encryption is thus:
    #   Interface > left > middle > right > reflector > right > middle > left > interface

    # Apply any necessary rotations
    leftRotor.applyRotation(letterIndex=letterIndex)

    middleRotor.applyRotation(letterIndex=letterIndex)

    rightRotor.applyRotation(letterIndex=letterIndex)

    # Get the initial input position from the interface
    interfacePosition = interface.getPositionFromLetter(letter=inputLetter)

    # Get the left rotor output position
    leftRotorOutputPosition = leftRotor.crossLeftToRight(inputPosition=interfacePosition)

    # Get the middle rotor output position
    middleRotorOutputPosition = middleRotor.crossLeftToRight(inputPosition=leftRotorOutputPosition)

    # Get the right rotor output position
    rightRotorOutputPosition = rightRotor.crossLeftToRight(inputPosition=middleRotorOutputPosition)

    # Get the reflector output position
    reflectorOutputPosition = reflector.crossLeftToRight(inputPosition=rightRotorOutputPosition)

    # Then we go back the other way

    # Get the right rotor input position
    rightRotorInputPosition = rightRotor.crossRightToLeft(outputPosition=reflectorOutputPosition)

    # Get the middle rotor input position
    middleRotorInputPosition = middleRotor.crossRightToLeft(outputPosition=rightRotorInputPosition)

    # Get the left rotor input position
    leftRotorInputPosition = leftRotor.crossRightToLeft(outputPosition=middleRotorInputPosition)

    # Get the interface output position
    interfaceOutputPosition = interface.crossRightToLeft(outputPosition=leftRotorInputPosition)

    # Get the output letter
    outputLetter = interface.getLetterFromPosition(position=interfaceOutputPosition)

    return outputLetter


if __name__ == "__main__":

    (
        interface,
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

    inputLetter = "A"
    letterIndex = 0

    outputLetter = encryptLetter(
        inputLetter=inputLetter,
        letterIndex=letterIndex,
        interface=interface,
        reflector=reflector,
        leftRotor=leftRotor,
        middleRotor=middleRotor,
        rightRotor=rightRotor
    )

    print(outputLetter)
