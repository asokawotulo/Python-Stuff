from authorClass import Author

class Book():
	def __init__(self, name, author_class, price, quantity):
		self.__name = name
		self.__authors = author_class
		self.__price = price
		self.__quantity = quantity
	
	# Getter Functions
	def getName(self):
		return self.__name
	def getAuthors(self):
		return self.__authors
	def getPrice(self):
		return self.__price
	def getQuantity(self):
		return self.__quantity

	# Setter Functions
	def setPrice(self, amount):
		self.__price = float(amount)
	def setQuantity(self, amount):
		self.__quantity = int(amount)

	# Output all Data
	def toString(self):
		return [self.__name, self.__authors, self.__price, self.__quantity]