class Account():
	def __init__(self, id, name, balance):
		self.__id = id
		self.__name = name
		self.__balance = balance

	def getID(self):
		return self.__id

	def getName(self):
		return self.__name

	def getBalance(self):
		return self.__balance

	def credit(self, amount):  
		self.__balance += amount
		return self.__balance

	def debit(self, amount):
		if amount <= self.__balance:
			self.__balance -= amount
		else:
			print("Amount exceeded balance")
		return self.__balance

	def transferTo(self, another, amount):
		if amount <= self.__balance:
			self.__balance -= amount
			another.credit(amount)
		else:
			print("Amount exceeded balance")
		return self.__balance

	def toString(self):
		print("ID:", self.__id)
		print("Name:", self.__name)
		print("Balance:", self.__balance)