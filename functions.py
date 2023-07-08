import time
from time import sleep
import os
import sys
import platform


######################################
#           MAIN FUNCTIONS           #
######################################

def clear_screen():
    opsys = platform.system()
    if(opsys == "Windows"):
        os.system('cls')
    else:
        os.system('clear')

def display_health(health):
    print("Health: "+str(health))

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



######################################
#        TRANSITION FUNCTIONS        #
######################################

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
