from classFile import *

def bankOptions():
	print("""Bank Options
[1] Login to Existing Account
[2] Create an Account
[3] Exit""")
	return int(input("Selected Option: "))

def login(index, bank_var):
	print("""Account Options
[1] Current Balance
[2] Deposit Money
[3] Withdraw Money
[4] Exit""")
	loginResponse = int(input("Selected Option: "))
	while loginResponse != 4:
		if loginResponse == 1:
			print(bank_var.getCustomer(index).getAccountBal())
		elif loginResponse == 2:
			amount = input("Deposit Amount: ")
			bank_var.getCustomer(index).setAccountDeposit(amount)
		elif loginResponse == 3:
			amount = input("Withdraw Amount: ")
			bank_var.getCustomer(index).setAccountWithdraw(amount)
		loginResponse = int(input("Selected Option: "))

def main():
	bank_var = Bank("Bank of Testing")
	bankResponse = bankOptions()
	while bankResponse != 3:
		if bankResponse == 1:
			firstName = input("First Name: ")
			lastName = input("Last Name: ")
			username = firstName.upper() + lastName.upper()
			password = input("Password: ")
			for i in bank_var.getCustomerList():
				usernameIndex = i.getUsername().index(username)
			if password == bank_var.getCustomer(usernameIndex).getPassword():
				print("Login Successful")
				login(usernameIndex, bank_var)
			else:
				print("Incorrect Password")
		elif bankResponse == 2:
			firstName = input("First Name: ")
			lastName = input("Last Name: ")
			password = input("Password: ")
			bank_var.addCustomers(firstName, lastName, password)
		bankResponse = bankOptions()
main()