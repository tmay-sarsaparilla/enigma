"""Module to define rotor class and a dictionary of available rotors"""

from string import ascii_uppercase
import pandas as pd
from random import choice, seed


class Rotor:
    """Class for an enigma machine rotor"""

    rotor_type = "rotor"

    def __init__(self, rotor_id, seed, initial_letter):

        self.id = rotor_id
        self.seed = seed
        self.initial_letter = initial_letter
        self.data = None
        self.rotations = 0
        self.period_of_rotation = 0

    def reset(self):
        """Method for resetting a rotor to it's initial state"""

        # Reset data and rotations
        self.data = None
        self.rotations = 0
        self.period_of_rotation = 0

    def set_initial_letter(self, initial_letter):
        """Method for setting the initial letter of a rotor"""

        self.initial_letter = initial_letter

        return

    def set_period_of_rotation(self, period_of_rotation):
        """Method for setting the period of rotation of a rotor"""

        self.period_of_rotation = period_of_rotation

        return

    def build_skeleton(self):
        """Method for building a rotor skeleton"""

        # Get list of all ASCII uppercase letters and list of possible positions
        letters = list(ascii_uppercase)
        positions = list(range(0, 26))

        # Build empty rotor table
        rotor = pd.DataFrame(
            columns=["letter", "position", "output_position"],
            index=letters
        )

        # Get index of seed letter in list
        initial_letter_index = letters.index(self.initial_letter)

        # Populate the letters column
        rotor["letter"] = letters
        # Populate the position column such that the seed letter is at position 0
        rotor["position"] = [(i - initial_letter_index) % 26 for i in positions]

        return rotor, letters, positions

    @staticmethod
    def pair_letters(rotor, letters, positions, chosen_letters):
        """Method for pairing letters together"""

        # Loop through each letter
        for i in letters:

            # If an output position has already been assigned, skip the letter
            if i in chosen_letters:

                continue

            # Find position of letter
            input_position = rotor.loc[i, "position"]

            # Randomly choose a position from the list (which is not the input position)
            output_position = choice([e for e in positions if e != input_position])

            # Assign position to letter
            rotor.loc[i, "output_position"] = output_position

            # Find the corresponding letter and complete the loop
            outputLetter = rotor[rotor["position"] == output_position].iloc[0]["letter"]

            rotor.loc[outputLetter, "output_position"] = input_position

            # Add both letters to the chosen letters list
            chosen_letters.append(i)
            chosen_letters.append(outputLetter)

            # Remove both input and output positions from possible choices
            positions.remove(input_position)
            positions.remove(output_position)

        return rotor

    def build(self):
        """Method for building a rotor"""

        # Build the skeleton rotor
        rotor, letters, positions = self.build_skeleton()

        # Set seed of the randomiser
        seed(self.seed)

        # Loop through each letter and assign a random output positions
        for i in letters:

            # Randomly choose a position from the list
            output_position = choice(positions)

            # Assign position to letter
            rotor.loc[i, "output_position"] = output_position

            # Remove position from possible choices
            positions.remove(output_position)

        # Assign the rotor data to the object
        self.data = rotor

        return

    def get_position_from_letter(self, letter):
        """Method to retrieve the position of a letter in a given rotor"""

        position = self.data.loc[letter, "position"]

        return position

    def get_letter_from_position(self, position):
        """Method to retrieve the letter of a position in a given rotor"""

        letter = self.data[self.data["position"] == position].iloc[0]["letter"]

        return letter

    def get_output_position_from_input_position(self, position):
        """Method to retrieve output position of a given rotor from a given input position"""

        letter = self.get_letter_from_position(position=position)

        output_position = self.data.loc[letter, "output_position"]

        return output_position

    def get_letter_from_output_position(self, output_position):
        """Method to retrieve letter of a given rotor from a given output position"""

        letter = self.data[self.data["output_position"] == output_position].iloc[0]["letter"]

        return letter

    def get_input_position_from_output_position(self, output_position):
        """Method to retrieve input position of a given rotor from a given output position"""

        letter = self.get_letter_from_output_position(output_position=output_position)

        position = self.get_position_from_letter(letter=letter)

        return position

    def should_rotate(self, letter_index):
        """Method for determining whether a rotor should rotate given an index and period"""

        should_rotate = False

        # If it's the first letter, don't rotate
        if letter_index == 0:

            return should_rotate

        # If the index is a multiple of the rotation, then rotate
        if letter_index % self.period_of_rotation == 0:

            should_rotate = True

        return should_rotate

    def rotate(self):
        """Method to rotate a rotor"""

        # Increase the rotor rotation by 1
        self.rotations += 1

        return

    def apply_rotation(self, letter_index):
        """Method to apply rotation to a rotor if necessary"""

        # Check if the rotor should be rotated
        if self.should_rotate(letter_index=letter_index):

            # Apply rotation
            self.rotate()

    def account_for_rotation_left_to_right(self, position):
        """Method to account for rotor rotation when crossing left to right"""

        # Calculate the rotated position
        rotated_position = (position + self.rotations) % 26

        return rotated_position

    def account_for_rotation_right_to_left(self, position):
        """Method to account for rotor rotation when crossing right to left"""

        # If the rotor has completed a full rotation, add 26 to avoid negative positions
        if position - self.rotations < 0:

            position += 26

        # Calculate the rotated position
        rotated_position = (position - self.rotations) % 26

        return rotated_position

    def cross_left_to_right(self, input_position):
        """Method to pass a letter across a rotor from left to right"""

        # Apply rotations to the input position
        rotated_input_position = self.account_for_rotation_left_to_right(input_position)

        # Get the output position
        output_position = self.get_output_position_from_input_position(rotated_input_position)

        # Apply rotations to the output position
        rotated_output_position = self.account_for_rotation_left_to_right(output_position)

        return rotated_output_position

    def cross_right_to_left(self, output_position):
        """Method to pass a letter across a rotor from right to left"""

        # Apply rotations to the output position
        rotated_output_position = self.account_for_rotation_right_to_left(output_position)

        # Get the input position
        input_position = self.get_input_position_from_output_position(rotated_output_position)

        # Apply rotations to the input position
        rotated_input_position = self.account_for_rotation_right_to_left(input_position)

        return rotated_input_position


class Interface(Rotor):
    """Class for the enigma interface"""

    rotor_type = "interface"

    def __init__(self, rotor_id, seed, initial_letter):

        super().__init__(rotor_id, seed, initial_letter)

    def build(self):
        """Method for building an interface rotor"""

        # Build the skeleton interface
        rotor, letters, positions = self.build_skeleton()

        # For the interface, output position is the same as input position
        rotor["output_position"] = rotor["position"]

        # Assign the rotor data to the object
        self.data = rotor

        return


class Reflector(Rotor):
    """Class for enigma reflector"""

    rotor_type = "reflector"

    def __init__(self, rotor_id, seed, initial_letter):

        super().__init__(rotor_id, seed, initial_letter)

    def build(self):
        """Method for building a reflector rotor"""

        # Build the skeleton reflector
        rotor, letters, positions = self.build_skeleton()

        # Set seed of the randomiser
        seed(self.seed)

        # For the reflector, inputs and outputs need to be paired together
        chosen_letters = []

        # Pair letters together
        rotor = self.pair_letters(rotor=rotor, letters=letters, positions=positions, chosen_letters=chosen_letters)

        # Assign the rotor data to the object
        self.data = rotor

        return


class Switchboard(Rotor):
    """Class for enigma switchboard"""

    rotor_type = "switchboard"

    def __init__(self, rotor_id, seed, initial_letter):

        super().__init__(rotor_id, seed, initial_letter)
        self.pairs = []

    def assign_pairs(self, pairs):
        """Method for assigning pairs of letters to the switchboard"""

        self.pairs = pairs

        return

    def build(self):
        """Method for building a switchboard"""

        # Build the skeleton switchboard
        rotor, letters, positions = self.build_skeleton()

        # Set the output position equal to the input position
        rotor["output_position"] = rotor["position"]

        # Check if there are pairs assigned to the switchboard
        if len(self.pairs) > 0:

            # Loop through the pairs
            for i in self.pairs:

                # Extract the letters in the pair
                first_letter = i[0]
                second_letter = i[1]

                # Find the position of the letters in the switchboard
                first_position = rotor.loc[first_letter, "position"]
                second_position = rotor.loc[second_letter, "position"]

                # Pair up the letters
                rotor.loc[first_letter, "output_position"] = second_position
                rotor.loc[second_letter, "output_position"] = first_position

        # Assign the rotor data to the object
        self.data = rotor

        return


if __name__ == "__main__":

    # Test interface
    interface_test = Interface(0, 0, "A")
    interface_test.build()
    print(interface_test.data)

    # Test switchboard
    switchboard_test = Switchboard(0, 2, "A")
    switchboard_pairs = [("A", "B")]
    switchboard_test.assign_pairs(switchboard_pairs)
    switchboard_test.build()
    print(switchboard_test.data)

    # Test rotor
    rotor_test = Rotor(1, 12, "G")
    rotor_test.build()
    print(rotor_test.data)

    # Test reflector
    reflector_test = Reflector(1, 86, "D")
    reflector_test.build()
    print(reflector_test.data)
