def operation(lists, oper, int_1, int_2):
	lists.append(int_1)
	lists.append(int_2)
	num_1 = lists.pop()
	num_2 = lists.pop()
	if(oper == "+"):
		result = num_2 + num_1
	elif(oper == "-"):
		result = num_2 - num_1
	elif(oper == "/"):
		result = num_2 / num_1
	elif(oper == "*"):
		result = num_2 * num_1
	lists.append(result)
	return int(result)

def nthoperation(lists, oper, int_1):
	lists.append(int_1)
	num_1 = lists.pop()
	num_2 = lists.pop()
	if(oper == "+"):
		result = num_2 + num_1
	elif(oper == "-"):
		result = num_2 - num_1
	elif(oper == "/"):
		result = num_2 / num_1
	elif(oper == "*"):
		result = num_2 * num_1
	lists.append(result)
	return int(result)

stack = []
oper = input("Operation: ")
num_1 = int(input("First Number: "))
num_2 = int(input("Second Number: "))

print("Result:", operation(stack, oper, num_1, num_2))

proceed = input("Would you like to do something with the previous number?")

while(proceed == "y"):
	oper = input("Operation: ")
	num_3 = int(input("Next Number: "))
	print("Result:", nthoperation(stack, oper, num_3))
	proceed = input("Would you like to do something with the previous number?")