from decimal import *

class Person:
	def __init__(self, name, address):
		self.__name = name
		self.__address = address

	# Getter Functions
	def getName(self):
		return self.__name
	def getAddress(self):
		return self.__name

	# Setter Functions
	def setAddress(self, new_address):
		self.__address = new_address

	# Output Function
	def toString(self):
		return "{}({})".format(self.__name, self.__address)

class Student(Person):
	def __init__(self, name, address):
		Person.__init__(self, name, address)
		self.__numCourses = 0
		self.__courses = []
		self.__grades = []

	# Add Function
	def addCourseGrade(self, course, grade):
		if course not in self.__courses:
			self.__numCourses += 1
			self.__courses.append(course)
			self.__grades.append(grade)
		else:
			return "Course already exists"

	# Getter Functions
	def getAverageGrades(self):
		if self.__numCourses > 0:
			double = Decimal(10) ** -2
			return Decimal(sum(self.__grades) / self.__numCourses).quantize(double)
		else:
			return "Insufficient number of courses"

	# Output Functions
	def printGrades(self):
		if self.__numCourses > 0:
			for i in range(self.__numCourses):
				double = Decimal(10) ** -2
				print("[{}] {} : {}".format(i+1, self.__courses[i], Decimal(self.__grades[i]).quantize(double)))
		else:
			return "Insufficient number of courses"
	def toString2(self):
		return "Student: " + self.toString()

class Teacher(Person):
	def __init__(self, name, address):
		Person.__init__(self, name, address)
		self.__courses = []

	# Setter Function
	def addCourse(self, course):
		if course in self.__courses:
			return False
		else:
			self.__courses.append(course)
			return True
	def removeCourse(self, course):
		if course not in self.__courses:
			return False
		else:
			del self.__courses[self.__courses.index(course)]
			return True

	# Output Functions
	def toString2(self):
		return "Teacher: " + self.toString()