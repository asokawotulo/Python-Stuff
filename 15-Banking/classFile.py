from decimal import *

def doubleNum(num):
	double = Decimal(10) ** -2
	return Decimal(num).quantize(double)

class Account:
	def __init__(self):
		self.__balance = doubleNum(0)

	# Getter Functions
	def getBalance(self):
		return self.__balance
	
	# Setter Functions
	def deposit(self, amount):
		doubleAmount = doubleNum(amount)
		if doubleAmount < 0:
			return False
		else:
			self.__balance += doubleNum(amount)
			return True
	def withdraw(self, amount):
		doubleAmount = doubleNum(amount)
		if doubleAmount > self.__balance:
			return False
		else:
			self.__balance -= doubleAmount
			return True

class Customer:
	def __init__(self, first, last, username, password):
		self.__firstName = first
		self.__lastName = last
		self.__password = password
		self.__username = username
		self.__account = Account()

	# Getter Functions
	def getFirstName(self):
		return self.__firstName
	def getLastName(self):
		return self.__lastName
	def getPassword(self):
		return self.__password
	def getUsername(self):
		return self.__username
	def getAccountBal(self):
		return self.__account.getBalance()
	def getAccount(self):
		return self.__account

	# Setter Functions
	def setAccount(self, acct):
		self.__account = Account(acct)
	def setAccountWithdraw(self, amount):
		return self.__account.withdraw(amount)
	def setAccountDeposit(self, amount):
		return self.__account.deposit(amount)

class Bank:
	def __init__(self, name):
		self.__customers = []
		self.__numberOfCustomers = 0
		self.__bankName = name

	# Getter Functions
	def getNumOfCustomers(self):
		return self.__numberOfCustomers
	def getCustomers(self, index):
		return "Full Name: {} {}\nBalance: {}".format(self.__customers[index].getFirstName(), self.__customers[index].getLastName(), self.__customers[index].getAccount())
	def getCustomer(self, index):
		return self.__customers[index]
	def getCustomerList(self):
		return self.__customers

	# Setter Functions
	def addCustomers(self, first, last, password):
		username = first.upper() + last.upper()
		userExists = False
		for i in self.__customers:
			if username == i.getUsername():
				userExists = True
			else:
				userExists = False
		if userExists == True:
			return False
		else:
			self.__numberOfCustomers += 1
			self.__customers.append(Customer(first, last, username, password))