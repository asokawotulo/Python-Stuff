from schoolClass import *
import sys

student_list = Student("Asoka", "Something")
teacher_list = Teacher("Jude", "Something2")

def login():
	login_as = input("Login as teacher/student? ").lower()
	if login_as == "teacher":
		password = input("Please input password: ")
		if password == "teacher123456":
			return "teacherTrue"
		else:
			login()
	elif login_as == "student":
		password = input("Please input password: ")
		if password == "student123456":
			return "studentTrue"
		else:
			login()
	else:
		login()

def studentOptions():
	print("#######################\n    Student Options    \n#######################")
	print("[1] Add course grade\n[2] Get grade average\n[3] Get Grades\n[4] Who am i? \n[5] Exit")
	return int(input("What would you like to do? "))

def teacherOptions():
	print("#######################\n    Teacher Options    \n#######################")
	print("[1] Add course\n[2] Remove course\n[3] Who am i? \n[4] Exit")
	return int(input("What would you like to do? "))

def main():
	login_response = login()
	if login_response == "studentTrue":
		studentResponse = studentOptions()
		while studentResponse != 5:
			if studentResponse == 1:
				courseName = input("Course Name: ")
				courseGrade = float(input("Course Grade: "))
				student_list.addCourseGrade(courseName, courseGrade)
			elif studentResponse == 2:
				print(student_list.getAverageGrades())
			elif studentResponse == 3:
				student_list.printGrades()
			elif studentResponse == 4:
				print(student_list.toString2())
			studentResponse = studentOptions()
		login_again = input("Would you like to login to another user? ").upper()
		if(login_again == "Y"):
			login_response = login()
		else:
			sys.exit()
	else:
		teacherResponse = teacherOptions()
		while teacherResponse != 4:
			if studentResponse == 1:
				courseName = input("Course Name: ")
				if teacher_list.addCourse(courseName) == True:
					print("Course Successfully Added")
				else:
					print("Course Already Exists")
			elif studentResponse == 2:
				courseName = input("Course Name: ")
				if teacher_list.addCourse(courseName) == True:
					print("Course Successfully Removed")
				else:
					print("Course Doesn't Exist")
			elif studentResponse == 3:
				print(student_list.toString2())
main()