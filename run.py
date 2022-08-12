"""
Used for libraries and imports
"""
import random

import sys  # used to exit the game

import os  # used to clear the screen

# Used to import a list of countries around the world
from words import country

import time  # Used to control the pace of the display

import colorama  # Used to import color for the text throughout the game
from colorama import Fore, Back, Style
colorama.init(autoreset=True)  # Resets the color everytime

import pyfiglet  # Used to create the opening and closing graphic

# Prints the title graphic
print(pyfiglet.figlet_format("Destination Unknown..."))


def introduction_message():
    """
    Welcomes the user, asks for their name and provides instructions
    about how Destination Unknown works. The user name requires the
    player to use only letters for their name
    """
    while True:
        name = input(f"{Fore.LIGHTGREEN_EX}What is your name?\n")
        clear_screen()
        if not name.isalpha():
            print(f"{Fore.LIGHTYELLOW_EX}Your name must be alphabetic only")
            continue
        else:
            print("\n")
            print(Fore.RESET + "* Destination unknown is a word guessing game.")
            print(" where you are trying to guess the name of a country!")
            print("\n")
            print("* Guess one letter at a time")
            print("\n")
            print("* Your chances will be based on 1.5 * the lenght of letters")
            print("in the countries name.")
            print("\n")
            print("* If you guess correct your chances remain the same.")
            print("\n")
            print("* If you guess incorrect then you will lose a chance")
            print("\n")
            print("* Correct letters will show up in the right order")
            print("to help you figure out the destination.")
            print("\n")
            print(f'Good luck, {Fore.LIGHTGREEN_EX}{name}!')
            print("\n")
            break


def choose_country():
    """
    Selects a random country from the words.py file and
    deselects any countries which name contails a space
    or a hyphen. Also returns a lower case word.
    """
    word = random.choice(country)

    while '-' in word or ' ' in word:
        word = random.choice(country)
    return word.lower()


def current_country(word, guesses):
    """
    If the players guess is corret the letter will show
    in the word. if not an asterik will show until the
    user guesses the correct letter eg. *a*a*a
    """
    current_country = ""
    for letter in word:
        if letter in guesses:
            current_country += letter
        else:
            current_country += "*"
    return current_country


# Variable to create graphic if the player guesses the country.
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


def start_game(word):
    """
    Function used to start and run the game. The includes the code
    for the player to take a guess, the amount of chances they have
    left and lets the user know if they have won or not.
    """
    # create an emply list to display player guesses
    player_guesses = []
    # Gives the player 1.5 times the lenght of the word to guess the country
    chances = len(word)*int(1.5)
    print("\n")
    print(Fore.LIGHTCYAN_EX + f'The destination has {str(len(word))} letters.')
    while True:
        if chances != 0:
            print("\nYou have " + str(chances) + " chances left.")
            time.sleep(1)
            print("\n")
            print("Country so far: " + current_country(word, player_guesses))
            time.sleep(1)
            print(Fore.LIGHTCYAN_EX + f'Used letters: {str(player_guesses)}')
            print("\n")
            guess = input("Guess:\n").lower()[0]

            if guess not in player_guesses:
                player_guesses.append(guess)
                clear_screen()

            if current_country(word, player_guesses) == word:
                print(Fore.LIGHTGREEN_EX + f'Yay! You guessed {word.upper()}!')
                print("\n")
                print(FIREWORKS)
               
                break

            else:
                if guess in word:
                    print("\n")
                    print(Fore.LIGHTGREEN_EX + "Correct letter!")
                else:
                    print("\n")
                    print(Fore.LIGHTYELLOW_EX + guess + " is not correct.")
                    chances -= 1
        else:
            print("\n")
            print(Fore.RED + "Hard luck! The destination was " + word.upper())
            break


def goodbye_message():
    """
    Final function which ends the game if the
    player wishes. It also prints Goodbye message
    with pyfiglet.
    """
    print(pyfiglet.figlet_format(f"Goodbye!"))
    sys.exit()


def play_again():
    """
    This function gives the user the option to play
    again or finish the game.
    """
    play_again = input("Would you like to play again? yes or no?/n")
    if play_again == ("yes"):
        choose_country()
    elif play_again == ("no"):
        print("Thanks you for playing")
        goodbye_message()
    else:
        print("Sorry invalid entry.")
       

def clear_screen():
    """
    Used to clear Terminal screen
    Credit: https://www.101computing.net/python-typing-text-effect/
    """
    os.system("clear")

while True:
    """
    Calls functions to run the game
    """
    word = choose_country()
    introduction_message()
    start_game(word)
    play_again()
