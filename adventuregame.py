from time import sleep
import os
import sys
wood = 0
diamond =0
health = 100

def typing(sentence):
    for x in sentence:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.05)
        if(x == "\n"):
            # press any key to continue?
            wait = input()
    

def dashboard(health): 
    #If using Windows os.system('cls')
    os.system('clear') 
    print("Health Level: ", health)

def dashboard_intro(location): 
    #If using Windows os.system('cls')
    os.system('clear') 
    print("Location: ", location)

# for intro scene: have user touch the amulet and have it glow so they know they have 
# become the chosen one

# maybe include a command sheet that the player has access to at all times
# that includes the keys they need to press to navigate through the game

location = "Beach" 
dashboard_intro(location)
typing("An amulet has been swept up on the beach by the village.\nYou bend down to pick it up.\n")
typing("Tiki, the local surfer, glances over at your direction.\nHe eyes the object in your hand.\n")
typing("Tiki: Oi Mate! I haven't seen you around here before, what's your name?\n")
name = input()
os.system('clear') 
typing("Tiki: I see the amulet in your hand.\nLet me take a closer look.\nI can't be belive my eyes, this amulet has been lost for years.\nWe need to tell the Chief.\n")
location = "Village"
dashboard_intro(location)
typing("Tiki takes you to the village...")
dashboard_intro(location)
typing("Tiki: Chief Koa! ")
typing(name)
typing(" has found the lost amulet.\n")
typing("Chief Koa: Thank heavens.\nOur village is facing its greatest crisis. \nThe trees are bare. \nThe fish in the sea are washing up on the shore. \nOur supplies are running out. \nOur people have lost their health.\n")
typing("You are the only one who can save our village.\nYou have to build a boat to get to the Island.\nYou will need these to collect *insert#of logs* log, *#of vines* vines,fabric to build a boat.\n")
typing("Take this backpack on your quest to store the items you collect along the way.")

take = ["x"]
print("Type 'x' to take the backpack.")


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

meetCaptainJack()

# Scene 6: Player encounters bad guys (threats) and fights them for fabric.




