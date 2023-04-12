import time
from time import sleep
import os
import sys
wood = 0
diamond =0
health = 100
l1='x'
l2=' '
l3=' '
l4=' '
stage=1

def forest_menu():
     print("1. Cut down a Tree\n")
     print("2. Build a Trap\n")

def current_location(l1,l2,l3,l4,stage):
    if(stage==1):
        print("["+l1+"]")
        print("Beach\n")
    if(stage==2):
        print("["+l1+"]\t["+l2+"]")
        print("Beach\tForest\n")
    if(stage==3):
        print("["+l1+"]\t["+l2+"]\t["+l3+"]")
        print("Beach\tForest\tSea\n")
    if(stage==4):
        print("["+l1+"]\t["+l2+"]\t["+l3+"]\t["+l4+"]")
        print("Beach\tForest\tSea\tIsland\n")

def typing(sentence):
    for x in sentence:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
        if(x == "\n"):
            # press any key to continue?
            wait = input()
    

def dashboard(health, location): 
    #If using Windows os.system('cls')
    os.system('clear') 
    if(location == "Coral Cove Beach"):
        print("[x]")
        print("Beach\n")



    print("Location: ", location)
    print("Health Level: ", health)


def dashboard_intro(location): 
    #If using Windows os.system('cls')
    os.system('clear') 
    if(location == "Coral Cove Beach"):
        print("[x]")
        print("Beach\n")
    
def animation():
    animation = [
        "[           ]",
        "[=          ]",
        "[===        ]",
        "[====       ]",
        "[=====      ]",
        "[======     ]",
        "[=======    ]",
        "[========   ]",
        "[=========  ]",
        "[========== ]",
        "[===========]",
        ]
    notcomplete = True
    i = 0
    while notcomplete:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.5)
        i += 1
        if i == 11:
            break

# for intro scene: have user touch the amulet and have it glow so they know they have 
# become the chosen one

# maybe include a command sheet that the player has access to at all times
# that includes the keys they need to press to navigate through the game
def scene1():
    location = "Coral Cove Beach" 
    dashboard_intro(location)
    typing("An amulet has been swept up on the beach by the village.\nYou bend down to pick it up.\n")
    typing("Tiki, the local surfer, glances over at your direction.\nHe eyes the object in your hand.\n")
    typing("Tiki: Oi Mate! I haven't seen you around here before, what's your name?\n")
    name = input("Type your name:")
    os.system('clear') 
    typing("Tiki: Welcome to Coral Cove ")
    typing(name)
    typing("!\n")
    typing("I saw you found something by the shore.\nLet me take a closer look...\nI can't be belive my eyes, this amulet has been lost for years.\nWe need to tell the Chief!\n")
    location = "Village"
    os.system('clear') 
    typing("Tiki takes you to the village...\n")
    animation()
    dashboard_intro(location)
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
    typing("I'm the forest ranger, my family has looked after the forest for many generation./n")
    typing("There are still many unknown mysteries of the forest yet to be discovered./n")
    typing("For your quest you will need the strongest wood to cross the sea./n")
    typing("Beware the strongest wood lies deep within the forest, where unknown creatures lurk./n")
    typing("Many strong people have ventured into the deep forest and have not returned./n")
    typing("The Chief said only you can save our our village. \nI wish you a safe journey ")
    typing(name)
    typing("!/n")
    typing("Enter 2 to continue into the forest")

    if (userinput =="2"):
        current_location(,x,,,2)


def scene2():
    location = "Dark Forest"
    os.system('clear') 
    typing("Walking to the dark forest...\n")
    animation()
    dashboard(location, health)
    forest_menu()


#Finish conversation with the chief and start the quest


#Do trades with characters in the forest.
# Scene 5: Player encounters a new character and trades wood for a rope
# Player is in the forest collecting wood. All of a sudden he hears footsteps, turns around
# and sees Captain Jack, a retired pirate who now runs a bar on the beach. He has an eyepatch
# and missing leg. You ask him if he has any rope. 

def forest():
    if userInput == "":
        meetCaptainJack()

# def trade():


def talkToJack():
    options = ["offer a trade", "walk away"]
    typing("Hey there! I'm Captain Jack. I was a pirate until my ship got attacked. My good 'ol leg also went down with the ship.")
    typing("\nNow I run a bar West of the Village. Come 'n stop by anytime!")
    userInput = "";
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

################GAME START#############
os.system('clear') 

