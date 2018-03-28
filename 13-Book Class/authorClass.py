class Author():
	def __init__(self, name, email, gender):
		self.__name = name
		self.__email = email
		self.__gender = gender
	
	def getName(self):
		return self.__name
	def getEmail(self):
		return self.__email
	def getGender(self):
		return self.__gender