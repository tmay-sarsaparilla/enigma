"""Module for saving user-defined configs"""

from pickle import dump, load, HIGHEST_PROTOCOL
from enigma.functions.config.default_config import default_config


if __name__ == "__main__":

    path = "/enigma/user_configs/user_config.pickle"

    with open(path, 'wb') as handle:

        dump(default_config, handle, protocol=HIGHEST_PROTOCOL)

    with open(path, 'rb') as handle:

        b = load(handle)

    print(b)
