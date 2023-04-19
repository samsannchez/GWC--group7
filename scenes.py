import time
from time import sleep
import os
import sys
from functions import typing, current_location, animation

name=""


# for intro scene: have user touch the amulet and have it glow so they know they have 
# become the chosen one

# maybe include a command sheet that the player has access to at all times
# that includes the keys they need to press to navigate through the game
def scene1():
    location = "Coral Cove Beach" 
    current_location("x","","","", 1)
    typing("An amulet has been swept up on the beach by the village.\nYou bend down to pick it up.\n")
    typing("Tiki, the local surfer, glances over at your direction.\nHe eyes the object in your hand.\n")
    typing("Tiki: Oi Mate! I haven't seen you around here before, what's your name?\n")
    name = input("Type your name:")
    os.system('clear') 
    typing("Tiki: Welcome to Coral Cove ")
    typing(name)
    typing("!\n")
    typing("I saw you found something by the shore.\nLet me take a closer look...\nI can't be belive my eyes, this amulet has been lost for years.\nWe need to tell the Chief!\n")
    os.system('clear') 
    typing("Tiki takes you to the village...\n")
    animation()
    os.system('clear') 
    current_location("x","","","", 1)
    typing("Tiki: Chief Koa! ")
    typing(name)
    typing(" has found the lost amulet.\n")
    typing("Chief Koa: Thank heavens.\n")
    typing("Our village is facing its greatest crisis. \nThe trees are bare. \nThe fish in the sea are washing up on the shore. \nOur supplies are running out. \nOur people have lost their health.\n")
    typing("You are the only one who can save our village.\nYou will have to venture into the dark forest.\n")
    typing("Take this backpack on your quest to store the items you collect along the way.\n")
    backpack=input("Type 'x' to take the backpack.")
     
#Scene 3 :Player meets a new character that will lead him into the forest
# The ranger informs you about the forest
#location forest unlocked
#The ranger:

def Ranger():
    typing("I'm the forest ranger, my family has looked after the forest for many generation.\n")
    typing("There are still many unknown mysteries of the forest yet to be discovered.\n")
    typing("For your quest you will need the strongest wood to cross the sea.\n")
    typing("Beware the strongest wood lies deep within the forest, where unknown creatures lurk.\n")
    typing("Many strong people have ventured into the deep forest and have not returned.\n")
    typing("The Chief said only you can save our our village. \nI wish you a safe journey ")
    typing(name)
    typing("!\n")

    userinput=typing("Enter 2 to continue into the forest")
    if (userinput == "2"):
        typing("Walking to the dark forest...\n")
        animation()
        current_location("","x","","",2)

def ignoreJack():
    print("User ignored Jack")

def talkToJack():
    options = ["offer a trade", "walk away"]
    typing("Hey there! I'm Captain Jack. I was a pirate until my ship got attacked. My good 'ol leg also went down with the ship.")
    typing("\nNow I run a bar West of the Village. Come 'n stop by anytime!")
    userInput = ""
    # while userInput not in options:
    #     print("\nOptions: offer a trade/walk away")
    #     userInput = input()

        # if userInput == "offer a trade"
        #     trade()

        # if userInput == "walk away"
        #     forest()

def meetCaptainJack():
    location = "forest"
    options = ["talk to jack", "ignore jack"]
    typing("\nYou hear footsteps behind you.\n")
    typing("You turn around and see Captain Jack, a retired pirate who now runs a bar on the beach.\n")
    typing("He has an eyepatch and a missing leg. ")
    typing("\nWhat would you like to do?")
    userInput = ""
    while userInput not in options:
        print("\nOptions: talk to jack/ignore jack")
        userInput = input()
        if userInput == "talk to jack":
            talkToJack()

        if userInput == "ignore jack":
            ignoreJack()



