"""Main module for enigma package"""
from enigma.__init__ import *

input_message = input("Write the message you want to encrypt: ")

output_message = encrypt(input_message=input_message, config=config)

print(output_message)
