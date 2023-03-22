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
   

dashboard(health)
typing("You are lost in the middle of the forest. There is a shinny object on the ground.")
a1 = input('''
1.Keep walking     2.Investigate\n''')
dashboard(health)
if(a1 == '2'):
    typing("You found a diamond!\nWould you like to put it on your backpack?")
    a1 = input("\n1.Yes     2.No\n")
    if(a1 == '1'):
        typing("Item collected!")
else:
    typing("You found wood!\nWould you like to put it on your backpack?")
    a1 = input("\n1.Yes     2.No")
    if(a1 == '1'):
        typing("Item collected!")
