import sys
import os
import random
import time
from time import sleep
import os
import sys

class TinyMazeEnv():

	# define status codes
	stepped = 1
	blocked = 2
	won = 3
	quit = 4
	tree = 9
	# define mazes
	mazes =	{ 
			  13: [ [ 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4],
			  		[ 4, 4, 4, 1, 0, 4, 4, 4, 4, 4, 4, 1, 1],
			  		[ 1, 0, 0, 0, 0, 1, 4, 4, 0, 4, 4, 1, 0],
			  		[ 0, 0, 1, 1, 3, 1, 0, 0, 0, 4, 1, 1, 0],
			  		[ 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 0],
			  		[ 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
			  		[ 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 3, 0, 0],
			  		[ 3, 1, 0, 0, 1, 1, 0, 2, 0, 0, 0, 1, 1],
			  		[ 0, 1, 1, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0],
			  		[ 0, 2, 0, 0, 1, 1, 3, 0, 0, 0, 1, 1, 1],
			  		[ 1, 0, 0, 0, 1, 1, 0, 0, 3, 0, 1, 0, 1],
			  		[ 1, 0, 1, 0, 0, 0, 2, 1, 1, 0, 1, 0, 1],
			  		[ 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] ],

			  11: [	[ 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
			 		[ 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
			 		[ 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
			 		[ 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
			 		[ 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
			 		[ 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
			 		[ 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
			 		[ 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
			 		[ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
			 		[ 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
			 		[ 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0] ],

		      9:  [	[ 0, 0, 1, 0, 0, 0, 0, 1, 1],
			 		[ 1, 0, 0, 0, 1, 1, 0, 0, 1],
			 		[ 0, 0, 1, 0, 0, 0, 0, 0, 1],
			 		[ 1, 0, 1, 0, 1, 0, 1, 0, 0],
			 		[ 0, 0, 0, 1, 1, 0, 0, 0, 1],
			 		[ 0, 1, 0, 0, 0, 1, 0, 1, 1],
			 		[ 0, 0, 0, 1, 0, 0, 0, 0, 1],
			 		[ 1, 0, 0, 0, 0, 1, 1, 0, 1],
			 		[ 0, 0, 1, 1, 0, 0, 0, 0, 0] ],	

			  7:  [ [ 0, 0, 1, 0, 0, 0, 0],
			 		[ 1, 0, 0, 0, 1, 1, 0],
			 		[ 0, 0, 1, 0, 0, 0, 0],
			 		[ 1, 0, 1, 0, 1, 0, 1],
			 		[ 0, 0, 0, 1, 1, 0, 0],
			 		[ 0, 1, 0, 0, 0, 1, 0],
			 		[ 0, 0, 0, 1, 0, 0, 0] ],

			  5:  [	[ 0, 2, 1, 0, 1],
					[ 1, 0, 1, 0, 0],
					[ 0, 0, 2, 0, 1],
					[ 0, 1, 1, 0, 1],
					[ 0, 2, 1, 0, 0] ]
			}

	
	def __init__(self,maze_size=13):
		# initialize starting position and maze
		self.x = 6
		self.y = 8
		self.total_steps = 0
		if maze_size in self.mazes.keys():
			self.maze = self.mazes[maze_size]
		else:
			self.maze = self.mazes[5]
		self.maze_size = len(self.maze)

	def display_maze(self,move='None'):
		character1=0
		# display the maze in its current state
		os.system('clear')  	# clear screen
		offset = " " * int((self.maze_size-5) * 1.5)
		print(offset + "        w: up")
		print(offset + "   a: left d: right")
		print(offset + "       s: down")
		print("")
		#print("---" * (self.maze_size + 2))
		for i in range(self.maze_size):
			row = "   "
			for j in range(self.maze_size):
				if i == self.y and j == self.x: 
					row += " U "
				elif self.maze[i][j] == 1: 
					row += " # "
				elif self.maze[i][j] == 2:
					row += " T "
				elif self.maze[i][j] == 3:
					row += " c "
				elif self.maze[i][j] == 4:
					row += "   "
				else: 
					row += " . "
			print(row)
			#print("---" * (self.maze_size + 2))
		#if(character1 != 0):
		#	print(offset + "You found a character!")
		#	character1 = 0
		#print(offset + "Move: {0}  Total steps: {1}".format(move,self.total_steps))
		#print(offset + "     x: {0}, y: {1}".format(self.x,self.y))

	def step(self,move):
		def typing(sentence):
			for x in sentence:
				print(x, end='')
				sys.stdout.flush()
				sleep(0.05)
				if(x == "\n"):
					# press any key to continue?
					wait = input()
			
		def meetcharacter():
			os.system('clear') 
			typing("This is a conversation with a character.\n")

		def collectwood():
			print(offset + "+5 Wood")

		# process a single action
		offset = " " * int((self.maze_size-5) * 1.5)
		self.total_steps += 1
		status = self.blocked
		if move == "a":
			if (self.x > 0) and (self.maze[self.y][self.x-1] != 1) and (self.maze[self.y][self.x-1] != 4): 
				self.x -= 1
				status = self.stepped
		elif move == "d":
			if (self.x < self.maze_size-1) and (self.maze[self.y][self.x+1] != 1) and (self.maze[self.y][self.x+1] != 4): 
				self.x += 1
				status = self.stepped
		elif move == "w":
			if (self.y > 0) and (self.maze[self.y-1][self.x] != 1) and (self.maze[self.y-1][self.x] != 4): 
				self.y -= 1
				status = self.stepped
		elif move == "s":
			if (self.y < self.maze_size-1) and (self.maze[self.y+1][self.x] != 1) and (self.maze[self.y+1][self.x] != 4): 
				self.y += 1
				status = self.stepped
		elif move == "Q":
			status = self.quit

		#Check for a character 
		if self.maze[self.y][self.x] == 3:
			meetcharacter()
			self.maze[self.y][self.x] = 10

		#Check for tree
		if self.maze[self.y][self.x] == 2:
			collectwood()
			self.maze[self.y][self.x] = 10

		return status

	def play(self):
		self.display_maze()
		offset = " " * int((self.maze_size-5) * 1.5)
		while True:
			if sys.version_info[0] < 3:
				move = raw_input()
			else:
				move = input()
			status = self.step(move)

			if status == self.quit: 
				print("You quit.")
				break
			else: 
				self.display_maze(move)


# main
if __name__ == "__main__":
	if len(sys.argv) > 1:
		maze = TinyMazeEnv(int(sys.argv[1]))
	else:
		maze = TinyMazeEnv()
	maze.play()