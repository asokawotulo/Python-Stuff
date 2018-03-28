from random import *

class Human:
	def __init__(self, name, equipment,health, hunger, energy, endurance, strength, speed, intelligence):
		# Basics
		self.name = name

		# Points
		self.max_healthPoints = health		#Maximum 25
		self.max_hungerPoints = hunger		#Maximum 25
		self.max_energyPoints = energy		#Maximum 25
		# Temp Points
		self.temp_healthPoints = health		#Maximum 25
		self.temp_hungerPoints = hunger		#Maximum 25
		self.temp_energyPoints = energy		#Maximum 25

		# Stats
		self.endurance = endurance			#Maximum 5
		self.strength = strength			#Maximum 5
		self.speed = speed					#Maximum 5
		self.intelligence = intelligence	#Maximum 5

		# Equipment
		self.equippedObject = equipment

	# Fighting Functions
	def attackTarget(self, target):
		chance = randint(0, 100)
		if chance <= 1:
			# 1% chance to get a 5 Multiplier
			attackMulti = 5
			print("Holy $hit are you even human!?")
		elif chance <= 15:
			# 15% chance to get a 3 Multiplier
			attackMulti = 3
			print("Super Critical Hit")
		elif chance <= 50:
			# 50% chance to get a 2 Multiplier
			attackMulti = 2
			print("Critical Hit")
		else:
			# Else get a 1 Multiplier
			attackMulti = 1
		attakPoints = (self.strength * attackMulti) + self.equippedObject["attackBonus"]
		target["temp_healthPoints"] -= attakPoints
		return "{}'s Health: {}".format(target["Name"], target["temp_healthPoints"])
	def attacked(self, target):
		chance = randint(0, 100)
		if chance <= 50:
			self.temp_healthPoints -= target["attack"]
	def runAway(self, target):
		if target["speed"] < self.speed:
			return True
		else:
			return False
	
	# Choosable Functions
	def searchForFood(self):
		chance = randint(0, 100)
		if chance <= 25:
			foodFound = 5
		elif chance <= 50:
			foodFound = 2
		else:
			foodFound = 0
		self.temp_energyPoints -= 2
		self.temp_hungerPoints -= 4
		return foodFound
	def doNothing(self):
		chance = randint(0, 3)
		nothingResponse = ["...", "...This is very unproductive...", "Why're you such a lazy ass", "I feel like i'm gonna die if I keep on doing this..."]
		return nothingResponse[chance]
	def doSleep(self):
		self.temp_energyPoints = self.max_energyPoints
		if self.temp_hungerPoints == self.max_hungerPoints:
			if self.temp_healthPoints < self.max_healthPoints:
				self.temp_healthPoints += 2
				return "Slept for a while... Energy replenished and Health + 2"
		return "Slept for a while... Energy replenished"
	def doEat(self, stock):
		stock -= 2
		self.temp_hungerPoints += 2

	# Getter Functions
	def getName(self):
		return self.name
	def getActions(self):
		return [["Search For Food", "Uses 2 Energy & 4 Hunger"], ["Sleep", "Replenish Energy"], ["Eat", "Consume 2 food"], ["Do Nothing", "You do nothing... Lazy ass"]]
	def getEnergy(self):
		return self.temp_energyPoints
	def getHealth(self):
		return self.temp_healthPoints
	def getHunger(self):
		return self.temp_hungerPoints

class Male(Human):
	def __init__(self, name, 
		equipment={"Name": "Fists", "attackBonus": 0}, 
		health=10, hunger=10, energy=10, 
		endurance=3, strength=3, speed=3, intelligence=3):
		Human.__init__(self, name, equipment, health, hunger, energy, endurance, strength, speed, intelligence)
	def getGender():
		return ["male", "him", "he", "boy"]

class Female(Human):
	def __init__(self, name, 
		equipment={"Name": "Fists", "attackBonus": 0}, 
		health=10, hunger=10, energy=10, 
		endurance=3, strength=3, speed=3, intelligence=3):
		Human.__init__(self, name, equipment, health, hunger, energy, endurance, strength, speed, intelligence)
	def getGender():
		return ["female", "her", "she", "girl"]