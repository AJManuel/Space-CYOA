import random
import math
import time, sys


def chooseOption(numberOfOptions):
    choice = 0
    while choice < 1 or choice > numberOfOptions:
        # print('1 to ' + str(numberOfOptions) + '> ', end='')
        choice = input()
        if choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = 0
        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            choice = int(choice)
        print('\n\n')
        return choice


def pause():
    input('Press enter to continue.\n')


def intro():
    print('\n')
    # Introduction
    print("This is a text-based choose your own adventure game.")
    print("Your choices affect the outcome of the game.")
    print("You will be asked questions as the story goes on to guide your adventure")
    pause()

    # starting the game
    start()


def start():
    time.sleep(0.5)
    print("You and your team have been tasked by the government to explore a place of your choice")
    print("You will have 4 choices on where you would like to visit")
    print("Would you like to visit:  ")
    print("1. \t Mars?")
    print("2. \t Pluto?")
    print("3. \t The Sun?")
    print("4. \t Saturn?")
    choice = chooseOption(5)
    if choice == 1:
        mars()
    elif 2 == choice:
        pluto()
    elif 3 == choice:
        sun()
    elif 4 == choice:
        saturn()
    else:
        print("Error")

def sun():
    print()
    print("Your team decided to visit the sun. Sadly, our technology has not prepared for dealing with the high heat of the sun.")
    print("Your team flies to close to the sun and burns to a crisp when it enters the atmosphere")
    print("Your mission is failed as you have died")

def saturn():
    print("Would you like to visit the rings or the surface?  ")
    print("1. \t Rings ")
    print("2. \t Surface ")
    choice = chooseOption(3)
    if choice == 1:
        rings()
    elif choice == 2:
        saturnSurface()
    else:
        print("Error")
        saturn()

def saturnSurface():
    print("As you land you have encountered a wild storm. Would would you like to do?")
    print("1. \t Escape and fly back home")
    print("2. \t Stay and brave the storm")
    choice = chooseOption(3)
    if choice == 1:
        escape()
    elif choice == 2:
        braveStorm()
    else:
        print("Error")
        saturnSurface()

def braveStorm():
    randNum = random.randrange(1, 101)
    if randNum >= 50:
        print("Good job on fighting out the storm to stay on saturn")
        print("Why dont you look around more and see if you can find anything")
        findAnimalSaturn()
    elif randNum <= 50:
        print("Whomp whomp")
    else:
        print("error")

smallCuteAnimal = r"""
  .|||||||||.          .|||||||||.
 |||||||||||||        |||||||||||||
|||||||||||' .\      /. `|||||||||||
`||||||||||_,__o    o__,_||||||||||'
"""
def findAnimalSaturn():
    print("While exploring Saturn you find a small, cute looking animal")
    print(smallCuteAnimal)
    print("What would you like to do with this animal?")
    print("1. \t Take it on the spaceship and head home ")
    print("2. \t Take pictures but go home without the unknown animal")
    choice = chooseOption(3)
    if choice == 1:
        homeWithAnimal()
    elif choice == 2:
        homeWithoutAnimal()
    else:
        print("Error")
        findAnimalSaturn()

def homeWithAnimal():
    print("You arrive home safely and are crowned as a scientific hero")
    print("You are famous worldwide")
    print("You are encouraged to go on another mission of you choosing, would you like to?")
    print("1. \t Go back on another mission")
    print("2. \t Finish and retire from being an astronaut")
    choice = chooseOption(3)
    if choice == 1:
        print("Very well")
        start()
    elif choice == 2:
        outro()
    else:
        print("Error")


def homeWithoutAnimal():
    print("You arrive home safely but the homebase is mad at you for not bringing back the creature")
    print("Despite this, they agree to let you go on another mission of your choosing, if you would like, would you?")
    print("1. \t Go back on another mission")
    print("2. \t Finish and retire from being an astronaut")
    choice = chooseOption(3)
    if choice == 1:
        print("Very well")
        start()
    elif choice == 2:
        outro()
    else:
        print("Error")

def outro():
    print("Thank you for playing my game")
    print("Have a good day")
    exit()


while True:
    # Start the game
    intro()

    # "Play again" user option
    print('\nWould you like to play again? Y/N')
    playAgain = input()
    if playAgain == 'Y' or playAgain == 'y':
        continue  # continue loop
    elif playAgain == 'N' or playAgain == 'n':
        outro()  # leave while loop
    else:
        print("Please read the instructions next time. Goodbye...")
        break

