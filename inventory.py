import os
import sys

#Declaring dictionary
mybackpack = {
  "wood": 0,
  "rope": 0,
  "fruit": 0
}

notmybackpack = {
	"wood": 5,
	"rope": 1,
	"fruit": 5,
	"cloth": 1,
}

#Add to inventory
def add_item(type, amount):
	# if type in mybackpack:
	new_amount = mybackpack[type]+amount
	mybackpack.update({type: new_amount})

	# mybackpack['type'] = amount



#Remove item from inventory
def remove_item(type, amount):
	new_amount=mybackpack[type]-amount
	mybackpack.update({type: new_amount})

#Remove all items from inventory 
def remove_all():
	mybackpack["wood"]=0
	mybackpack["rope"]=0
	mybackpack["fruit"]=0

#Display inventory
def display_inventory():
	# os.system('clear')
	print("---My Backpack---")
	print("wood: " + str(mybackpack["wood"]))
	print("rope: " + str(mybackpack["rope"]))
	print("fruit: " + str(mybackpack["fruit"]))
	# print("press enter to return to map")
	goback=input()

def display_character_inventory(name):
	print("---" + name + "'s Backpack---")
	for key, values in notmybackpack.items():
		print(str(key) + ": " + str(values))
	
	# goback = input()




