import os
import sys

#Declaring dictionary
mybackpack = {
  "wood": 0,
  "rope": 0,
  "fruit": 0
}

#Add to inventory
def add_item(type, amount):
	new_amount=mybackpack[type]+amount
	mybackpack.update({type: new_amount})

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
	os.system('clear')
	print("----Backpack----")
	print("wood: " + str(mybackpack["wood"])+"\n")
	print("rope: " + str(mybackpack["rope"])+"\n")
	print("fruit: " + str(mybackpack["fruit"])+"\n")
	goback=input()
