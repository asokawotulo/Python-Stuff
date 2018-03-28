from accountClass import Account

account_list = [Account("0", "Andrew", 1000), Account("1", "Asoka", 1000)]

def decision_list():
	print("""
Decision List
[1] Account Info
[2] Transfer
[3] Deposit
[4] Withdraw
[5] Exit
""")

def main():
	global account_list
	account_login = int(input("Input ID to login to: "))
	decision_list()
	decision = int(input("Input Decision: "))
	while(decision != 5):
		if(decision == 1):
			print("######################\n#    Account Info    #\n######################")
			account_list[account_login].toString()
		elif(decision == 2):
			print("#################\n#    Transfer    #\n#################")
			account_ID = int(input("Account ID: "))
			amount = int(input("Amount: "))
			account_list[account_login].transferTo(account_list[account_ID], amount)
		elif(decision == 3):
			print("###############\n#    Deposit    #\n###############")
			amount = int(input("Amount: "))
			account_list[account_login].credit(amount)
		elif(decision == 4):
			print("###############\n#    Withdraw    #\n###############")
			amount = int(input("Amount: "))
			account_list[account_login].debit(amount)
		decision_list()
		decision = int(input("Input Decision: "))
	print("Thank you for using me")
	replay = input("Would you like to login to another account? (Y/N) ")
	if(replay.upper() == "Y"):
		main()
	else:
		pass
main()