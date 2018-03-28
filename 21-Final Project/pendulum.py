from numpy import radians

class Pendulum():

	def __init__(self):
		# Pendulum Variables
		self.__length_one = float(input("Insert length of Pendulum 1: "))
		self.__length_two = float(input("Insert length of Pendulum 2: "))
		self.__mass_one = float(input("Insert mass of Pendulum 1: "))
		self.__mass_two = float(input("Insert mass of Pendulum 2: "))

		# Initial theta (degrees)
		self.__theta_one = float(input("Insert initial angle of Pendulum 1: "))
		self.__theta_two = float(input("Insert initial angle of Pendulum 2: "))

		# Initial angular velocity (degrees/s)
		self.__omega_one = float(input("Insert initial angular velocity of Pendulum 1: "))
		self.__omega_two = float(input("Insert initial angular velocity of Pendulum 2: "))

		# Initial state
		self.__state = radians([self.__theta_one, self.__omega_one, self.__theta_two, self.__omega_two])

	def get_length_one(self):
		return self.__length_one

	def get_length_two(self):
		return self.__length_two

	def get_mass_one(self):
		return self.__mass_one

	def get_mass_two(self):
		return self.__mass_two

	def get_state(self):
		return self.__state
