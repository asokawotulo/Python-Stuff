from Classes.classHuman import *
from random import *
import time
import os

listOfHumans = [Male("Adam"), Female("Eve")]
listOfAnimals = [{"Name": "Boar", "healthPoints": 15, "temp_healthPoints": 15, "speed": 2, "attack": 5, "foodBonus": 5}]

def encounterAnimal():
	encounterChance = randint(0, 100)
	if encounterChance <= 50:
		animalIndex = randint(0, len(listOfAnimals)-1)
		print("You encountered a", listOfAnimals[animalIndex]["Name"])
		print("What would are you gonna do?\n[1] Attack Animal\n[2] Run Away")
		response = int(input())
		if response == 1:
			return ["attackTarget", listOfAnimals[animalIndex]]
		elif response == 2:
			return ["runAway", listOfAnimals[animalIndex]]
	else:
		return [""]

def fightOrflight(encounter, chosen):
	if encounter[0] == "runAway":
		chosen.runAway(encounter[1])
		return 0
	elif encounter[0] == "attackTarget":
		encounter[1]["temp_healthPoints"] = encounter[1]["healthPoints"]
		while encounter[1]["temp_healthPoints"] > 0:
			chosen.attacked(encounter[1])
			print("{}'s Health: {}".format(chosen.getName(), chosen.getHealth()))
			print(chosen.attackTarget(encounter[1]))
			print()
			time.sleep(1)
		return encounter[1]["foodBonus"]
	return 0

def clearScreen():
	os.system("clear")

def greeting():
	print("Welcome to the Survivor Simulation")
	print("\nFor some unexplained reason the world has no more than 2 humans.\nChoose a character you would like to become:")

def autoDecision(character, food):
	if food < 5:
		foodFound = character.searchForFood()
		print("{} found {} food".format(character.getName(), foodFound))
		return foodFound
	elif character.getHunger() < 10:
		character.doEat(food)
		print(character.getName(), "ate some food")
	elif character.getEnergy() < 10:
		character.doSleep()
		print(character.getName(), "slept")
	else:
		character.doNothing()
		print(character.getName(), "did nothing")

def getAllStats(list):
	print("Stats of each person:")
	for i in list:
		print("--" + i.getName())
		print("Health:", i.getHealth())
		print("Hunger:", i.getHunger())
		print("Energy:", i.getEnergy())

def chooseCharacter():
	greeting()
	for i in range(len(listOfHumans)):
		print("[{}] {}".format(i+1, listOfHumans[i].getName()))

	charSelect = int(input("Insert number: "))
	if 1 <= charSelect <= 2:
		print("\nYou have selected [ {} ]\n".format(listOfHumans[charSelect-1].getName()))

	return charSelect - 1

def main():
	chosenIndex = chooseCharacter()
	chosenCharacter = listOfHumans[chosenIndex]
	unchosenCharacter = listOfHumans[chosenIndex-1]
	iteration = 1
	food_stock = 0
	while iteration <= 10 and chosenCharacter.getHealth() > 0 and unchosenCharacter.getHealth() > 0: # 10 Iterations in the game
		clearScreen()

		print("###############\nIt's a new day!\nDAY", iteration)
		print("Amount of food in stock:", food_stock)

		iteration2 = 0
		while iteration2 != 4 and chosenCharacter.getHealth() > 0 and unchosenCharacter.getHealth() > 0: # You can do 4 actions per iteration
			print("List of things you can do")
			print("Action {}/4".format(iteration2))

			for i in range(len(chosenCharacter.getActions())):
				print("[{}] {} ({})".format(i+1, chosenCharacter.getActions()[i][0], chosenCharacter.getActions()[i][1]))
			print("[5] Get Stats")
			
			actionChosen = int(input("Chosen action: "))
			
			print("###############")
			
			if actionChosen == 1:
				if chosenCharacter.getEnergy() < 3 or chosenCharacter.getHunger() < 5:
					print("!!!Not enough Energy and/or Hunger!!!")
				else:
					encounter = encounterAnimal()
					foodFound = chosenCharacter.searchForFood()
					foodFound += int(fightOrflight(encounter, chosenCharacter))
					unchosenDecision = autoDecision(unchosenCharacter, food_stock)
					if isinstance(unchosenDecision, int):
						food_stock += unchosenDecision
					print("You found {} food".format(foodFound))
					food_stock += foodFound
					iteration2 += 1
			elif actionChosen == 2:
				unchosenDecision = autoDecision(unchosenCharacter, food_stock)
				if isinstance(unchosenDecision, int):
					food_stock += unchosenDecision
				print(chosenCharacter.doSleep())
				iteration2 += 2
			elif actionChosen == 3:
				unchosenDecision = autoDecision(unchosenCharacter, food_stock)
				if isinstance(unchosenDecision, int):
					food_stock += unchosenDecision
				chosenCharacter.doEat(food_stock)
				print("You ate some food")
				iteration2 += 1
			elif actionChosen == 4:
				unchosenDecision = autoDecision(unchosenCharacter, food_stock)
				if isinstance(unchosenDecision, int):
					food_stock += unchosenDecision
				print(chosenCharacter.doNothing())
				iteration2 += 1
			elif actionChosen == 5:
				print("Amount of food in stock:", food_stock)
				getAllStats(listOfHumans)
		iteration += 1
		print("You Lost... Fucking loser")

main()