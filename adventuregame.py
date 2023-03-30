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

def dashboard(health): 
    #If using Windows os.system('cls')
    os.system('clear') 
    print("Health Level: ", health)

def dashboard_intro(location): 
    #If using Windows os.system('cls')
    os.system('clear') 
    print("Location: ", location)

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
typing("Chief Koa: Thank heavens.\nOur village is facing its greatest crisis. \nThe trees are bare. \nThe fish in the sea are washing up on the shore. \nOur supplies are running out. \nOur people have lost their health.")
typing("The only one who can save our village is you.\nYou have to build a boat to get to the Island.\nYou will need these to collect *insert#of logs* log, *#of vines* vines,fabric to build a boat.\n")
typing("Take this backpack on your quest to store the items you collect along the way.")

#Finish conversation with the chief and start the quest

#Do trades with characters in the forest.


