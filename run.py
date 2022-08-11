# Used to choose a random country for the game
import random

# Used to exit the game when the player chooses
# not to continue at the end
import sys

# Used to import a list of countries around the world
from words import country

# Used to import color for the text throughout the game
import colorama
from colorama import Fore, Back, Style
# Resets the color everytime
colorama.init(autoreset=True)

# Used to create the opening and closing graphic
import pyfiglet

# Prints the title graphic
print(pyfiglet.figlet_format("Destination Unknown..."))

# Selects a random country from the words.py file and 
# deselects any countries which name contails a space
# or a hyphen. Also returns a lower case word. 

def choose_word():
    word = random.choice(country)
    while '-' in word or ' ' in word:
        word= random.choice(country)
    return word.lower()

