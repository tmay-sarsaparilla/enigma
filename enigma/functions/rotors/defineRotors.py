"""Module to define rotor class and a dictionary of available rotors"""

from string import ascii_uppercase
import pandas as pd
from random import choice, seed


class Rotor:
    """Class for an enigma machine rotor"""

    def __init__(self, rotorId, seedLetter):

        self.id = rotorId
        self.seedLetter = seedLetter
        self.data = None
        self.rotations = 0
        self.periodOfRotation = 0

    def getSeedLetter(self):
        """Method for retrieving the seed letter of a rotor"""

        return self.seedLetter

    def setPeriodOfRotation(self, periodOfRotation):
        """Method for setting the period of rotation of a rotor"""

        self.periodOfRotation = periodOfRotation

        return

    def build(self):
        """Method for building a rotor"""

        # Get list of all ASCII uppercase letters and list of possible positions
        letters = list(ascii_uppercase)
        positions = list(range(0, 26))

        # Build empty rotor table
        rotor = pd.DataFrame(
            columns=["letter", "position", "outputPosition"],
            index=letters
        )

        # Get index of seed letter in list
        seedLetterIndex = letters.index(self.seedLetter)

        # Populate the letters column
        rotor["letter"] = letters
        # Populate the position column such that the seed letter is at position 0
        rotor["position"] = [(i - seedLetterIndex) % 26 for i in positions]

        # Set seed of the randomiser
        seed(seedLetterIndex)

        # Loop through each letter and assign a random output positions
        for i in letters:

            # Randomly choose a position from the list
            outputPosition = choice(positions)

            # Assign position to letter
            rotor.loc[i, "outputPosition"] = outputPosition

            # Remove position from possible choices
            positions.remove(outputPosition)

        self.data = rotor

        return

    def getPositionFromLetter(self, letter):
        """Method to retrieve the position of a letter in a given rotor"""

        position = self.data.loc[letter, "position"]

        return position

    def getLetterFromPosition(self, position):
        """Method to retrieve the letter of a position in a given rotor"""

        letter = self.data[self.data["position"] == position].iloc[0]["letter"]

        return letter

    def getOutputPositionFromInputPosition(self, position):
        """Method to retrieve output position of a given rotor from a given input position"""

        letter = self.getLetterFromPosition(position=position)

        outputPosition = self.data.loc[letter, "outputPosition"]

        return outputPosition

    def getLetterFromOutputPosition(self, outputPosition):
        """Method to retrieve letter of a given rotor from a given output position"""

        letter = self.data[self.data["outputPosition"] == outputPosition].iloc[0]["letter"]

        return letter

    def getInputPositionFromOutputPosition(self, outputPosition):
        """Method to retrieve input position of a given rotor from a given output position"""

        letter = self.getLetterFromOutputPosition(outputPosition=outputPosition)

        position = self.getPositionFromLetter(letter=letter)

        return position

    def shouldRotate(self, letterIndex):
        """Method for determining whether a rotor should rotate given an index and period"""

        shouldRotate = False

        # If it's the first letter, don't rotate
        if letterIndex == 0:

            return shouldRotate

        # If the index is a multiple of the rotation, then rotate
        if letterIndex % self.periodOfRotation == 0:

            shouldRotate = True

        return shouldRotate

    def rotate(self):
        """Method to rotate a rotor"""

        # Increase the rotor rotation by 1
        self.rotations += 1

        return

    def applyRotation(self, letterIndex):
        """Method to apply rotation to a rotor if necessary"""

        # Check if the rotor should be rotated
        if self.shouldRotate(letterIndex=letterIndex):

            # Apply rotation
            self.rotate()

    def accountForRotationLeftToRight(self, position):
        """Method to account for rotor rotation when crossing left to right"""

        # Calculate the rotated position
        rotatedPosition = (position + self.rotations) % 26

        return rotatedPosition

    def accountForRotationRightToLeft(self, position):
        """Method to account for rotor rotation when crossing right to left"""

        # If the rotor has completed a full rotation, add 26 to avoid negative positions
        if position - self.rotations < 0:

            position += 26

        # Calculate the rotated position
        rotatedPosition = (position - self.rotations) % 26

        return rotatedPosition

    def crossLeftToRight(self, inputPosition):
        """Method to pass a letter across a rotor from left to right"""

        # Apply rotations to the input position
        rotatedInputPosition = self.accountForRotationLeftToRight(inputPosition)

        # Get the output position
        outputPosition = self.getOutputPositionFromInputPosition(rotatedInputPosition)

        # Apply rotations to the output position
        rotatedOutputPosition = self.accountForRotationLeftToRight(outputPosition)

        return rotatedOutputPosition

    def crossRightToLeft(self, outputPosition):
        """Method to pass a letter across a rotor from right to left"""

        # Apply rotations to the output position
        rotatedOutputPosition = self.accountForRotationRightToLeft(outputPosition)

        # Get the input position
        inputPosition = self.getInputPositionFromOutputPosition(rotatedOutputPosition)

        # Apply rotations to the input position
        rotatedInputPosition = self.accountForRotationRightToLeft(inputPosition)

        return rotatedInputPosition


class Interface(Rotor):
    """Class for the enigma interface"""

    def __init__(self, rotorId, seedLetter):

        super().__init__(rotorId, seedLetter)

    def build(self):
        """Method for building an interface rotor"""

        # Get list of all ASCII uppercase letters and list of possible positions
        letters = list(ascii_uppercase)
        positions = list(range(0, 26))

        # Build empty rotor table
        rotor = pd.DataFrame(
            columns=["letter", "position", "outputPosition"],
            index=letters
        )

        # Get index of seed letter in list
        seedLetterIndex = letters.index(self.seedLetter)

        # Populate the letters column
        rotor["letter"] = letters
        # Populate the position column such that the seed letter is at position 0
        rotor["position"] = [(i - seedLetterIndex) % 26 for i in positions]

        # For the interface, output position is the same as input position
        rotor["outputPosition"] = rotor["position"]

        self.data = rotor

        return


class Reflector(Rotor):
    """Class for enigma reflector"""

    def __init__(self, rotorId, seedLetter):

        super().__init__(rotorId, seedLetter)

    def build(self):
        """Method for building a reflector rotor"""

        # Get list of all ASCII uppercase letters and list of possible positions
        letters = list(ascii_uppercase)
        positions = list(range(0, 26))

        # Build empty rotor table
        rotor = pd.DataFrame(
            columns=["letter", "position", "outputPosition"],
            index=letters
        )

        # Get index of seed letter in list
        seedLetterIndex = letters.index(self.seedLetter)

        # Populate the letters column
        rotor["letter"] = letters
        # Populate the position column such that the seed letter is at position 0
        rotor["position"] = [(i - seedLetterIndex) % 26 for i in positions]

        # For the reflector, inputs and outputs need to be paired together
        chosenLetters = []

        for i in letters:

            # Find position of letter
            inputPosition = rotor.loc[i, "position"]

            # If an output position has already been assigned, skip the letter
            if i in chosenLetters:

                continue

            # Randomly choose a position from the list (which is not the input position)
            outputPosition = choice([e for e in positions if e != inputPosition])

            # Assign position to letter
            rotor.loc[i, "outputPosition"] = outputPosition

            # Find the corresponding letter and complete the loop
            outputLetter = rotor[rotor["position"] == outputPosition].iloc[0]["letter"]

            rotor.loc[outputLetter, "outputPosition"] = inputPosition

            # Add both letters to the chosen letters list
            chosenLetters.append(i)
            chosenLetters.append(outputLetter)

            # Remove both input and output positions from possible choices
            positions.remove(inputPosition)
            positions.remove(outputPosition)

        self.data = rotor

        return


# Define rotors configurations
interface = Interface(0, "A")

rotor1 = Rotor(1, "B")
rotor2 = Rotor(2, "Q")
rotor3 = Rotor(3, "J")
rotor4 = Rotor(4, "V")
rotor5 = Rotor(5, "A")

reflector1 = Reflector(1, "C")
reflector2 = Reflector(2, "K")

# Build dictionaries
rotorDict = {

    1: rotor1,
    2: rotor2,
    3: rotor3,
    4: rotor4,
    5: rotor5

}

reflectorDict = {

    1: reflector1,
    2: reflector2

}


if __name__ == "__main__":

    rotor_config = Rotor(1, "G")
    rotor_config.build()
    print(rotor_config.data)

    interface_config = Interface(0, "A")
    interface_config.build()
    print(interface_config.data)

    reflector_config = Reflector(1, "C")
    reflector_config.build()
    print(reflector_config.data)
