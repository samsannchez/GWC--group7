import os
import sys
from scenes import scene1, Ranger, talkToJack, meetCaptainJack
import maze
import Island_Maze
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
#scene1()
#Ranger()
#game=maze.TinyMazeEnv()
#game.play()
game2 = Island_Maze.TinyMazeEnv()
game2.play()
