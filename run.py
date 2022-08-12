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

# Function to show correct letter guessed in the correct position in the current country
def current_country(word, guesses):
    current_country = ""
    for letter in word:
        if letter in guesses:
            current_country =+ letter
        else:
            current_country =+ "*"
    return current_country

# Global variable used to create a fun display if the user guesses the correct country
FIREWORKS = """
                                 .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Main funtion to run the word game. This includes the code for the player too
# input their name, take a guess, the amount of chances they have left and
# lets the user know if they have won or not

def start_game(word):
    # create an emply list to display player guesses 
    player_guesses = []
    # Gives the player 1.5 times the lenght of the word to guess the country
    chances = len(word)*int(1.5)
