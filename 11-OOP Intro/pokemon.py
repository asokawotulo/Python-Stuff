class Pokemon:
	def __init__(self, name, type, gender, hp, level):
		self.__name = name
		self.__type = type
		self.__gender = gender
		self.__hp = hp
		self.__level = level
		self.__location = [0, 0]
	
	def walk(self):
		print("Walking...")

	def attack(self):
		print("Attacking...")
	
	def eat(self):
		print("Eating...")
	
	def sleep(self):
		print("Sleeping...")
	
	def run(self):
		print("Running...")
	
	def getLocation(self):
		return self.__location

	def resetLocation(self):
		self.__location[0] = 0
		self.__location[1] = 0

	def changeLocation(self, x, y):
		self.__location[0] += x
		self.__location[1] += y