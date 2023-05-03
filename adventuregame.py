import os
import sys
from scenes import scene1, Ranger, talkToJack, meetCaptainJack
import maze
wood = 0
diamond =0
health = 100
l1='x'
l2=' '
l3=' '
l4=' '
stage=1


######################################
#             GAME START             #
######################################
# os.system('clear') 
# scene1()
# Ranger()
# os.system('clear') 
game=maze.TinyMazeEnv()
game.play()
