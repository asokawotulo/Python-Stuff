from bookClass import *

def addAuthor():
	global author_list
	authorName = input("Author Name: ")
	authorEmail = input("Author Email: ")
	authorGender = input("Author Gender: ")
	author_list.append(Author(authorName, authorEmail, authorGender))

def decision_list():
	print("""
Decision List
[1] Add a Book
[2] See Book List
[3] Edit Book Properties
[4] Exit
""")

book_list = [Book("Something", Author("Asoka", "something@gmail.com", "M"), 199.99, 10)]

decision_list()
decision = int(input("Input Decision: "))

while decision != 4:
	if decision == 1:
		author_list = []
		bookName = input("Book Name: ")
		bookPrice = float(input("Book Price: "))
		bookQuantity = int(input("Book Quantity: "))
		authorNum = int(input("How many authors are there? "))
		if authorNum > 1:
			for _ in range(authorNum):
				addAuthor()
		else:
			addAuthor()
			book_list.append(Book(bookName, author_list[0], bookPrice, bookQuantity))
	
	elif decision == 2:
		for i in range(len(book_list)):
			print("[{}] {}".format(i + 1, book_list[i].getName()))
		
		if len(book_list) > 0 and input("Would you like to see more info? (Y/N) ") == "Y":
			more_index = int(input("Choose a book from the list: "))
			book_select = book_list[more_index - 1]
			print("Book Name: ", book_select.toString()[0])
			print("Book Price: ", book_select.toString()[2])
			print("Book Quantity: ", book_select.toString()[3])
			print("Author Name: ", book_select.toString()[1].getName())
			print("Author Email: ", book_select.toString()[1].getEmail())
			print("Author Gender: ", book_select.toString()[1].getGender())
	
	elif decision == 3:
		print("[1] Price\n[2] Quantity")
		edit_select = int(input("Which would you like to edit? "))
		if edit_select == 1:
		elif edit_select == 2:
		else:
			print("")
	
	decision_list()
	decision = int(input("Input Decision: "))