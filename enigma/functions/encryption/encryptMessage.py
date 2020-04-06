"""Module to encrypt a message"""
from enigma.functions.encryption.encryptLetter import encryptLetter
from enigma.functions.rotors.constructRotors import constructRotors
from string import punctuation, whitespace
from textwrap import wrap


def cleanseInputMessage(inputMessage):
    """Function for cleansing an input message"""

    # Remove punctuation or whitespace
    for i in punctuation + whitespace:

        inputMessage = inputMessage.replace(i, "")

    # Make upper case
    inputMessage = inputMessage.upper()

    # Check for numbers
    if not inputMessage.isalpha():

        raise ValueError("Message cannot contain numerals")

    return inputMessage


def encrypt(
        inputMessage,
        reflectorId,
        leftRotorId,
        middleRotorId,
        rightRotorId
):
    """Function to encrypt a message using a given configuration of rotors"""

    # Prepare the rotors
    (
        interface,
        switchboard,
        leftRotor,
        middleRotor,
        rightRotor,
        reflector
    ) = constructRotors(
                        reflectorId=reflectorId,
                        leftRotorId=leftRotorId,
                        middleRotorId=middleRotorId,
                        rightRotorId=rightRotorId
                        )

    # Initialise the encrypted message
    encryptedLetters = ""

    # Cleanse the input message
    preparedMessage = cleanseInputMessage(inputMessage)

    messageLetters = list(preparedMessage)

    # Loop through each letter in the message
    for i in range(0, len(messageLetters)):

        # Retrieve the letter and index
        letter = messageLetters[i]
        letterIndex = i

        # Encrypt the letter
        outputLetter = encryptLetter(
                                     inputLetter=letter,
                                     letterIndex=letterIndex,
                                     interface=interface,
                                     switchboard=switchboard,
                                     reflector=reflector,
                                     leftRotor=leftRotor,
                                     middleRotor=middleRotor,
                                     rightRotor=rightRotor
                                     )

        # Add to the encrypted string
        encryptedLetters += outputLetter

    # Break the encrypted string into chunks of 5 letters
    encryptedList = wrap(encryptedLetters, 5)

    # Collapse into single string with spaces between chunks
    encryptedMessage = " ".join(encryptedList)

    return encryptedMessage


if __name__ == "__main__":

    inputMessage = "VCIUS FKIMX"

    reflectorId = 1

    leftRotorId = 1
    middleRotorId = 2
    rightRotorId = 3

    encryptedMessage = encrypt(
                               inputMessage=inputMessage,
                               reflectorId=reflectorId,
                               leftRotorId=leftRotorId,
                               middleRotorId=middleRotorId,
                               rightRotorId=rightRotorId
                               )

    print(encryptedMessage)
