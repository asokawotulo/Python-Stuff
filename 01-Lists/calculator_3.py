def push(stack, value):
	stack.append(value)
	
def pull(stack):
	return stack.pop()
	
def add(stack, num_1, num_2):
	result = num_2 + num_1
	push(stack, int(result))
	return int(result)
	
def minus(stack, num_1, num_2):
	result = num_2 - num_1
	push(stack, int(result))
	return int(result)
	
def multiply(stack, num_1, num_2):
	result = num_2 * num_1
	push(stack, int(result))
	return int(result)
	
def divide(stack, num_1, num_2):
	result = num_2 / num_1
	push(stack, int(result))
	return int(result)
	
def check_stack(stack, oper):
	if(len(stack) < 2):
		print("Please input more than 2 numbers")
	else:
		num_1 = pull(stack)
		num_2 = pull(stack)
		print(oper(stack, num_1, num_2))

def delete_stack(stack):
	del stack[:]

lists = []
print("""RNP Calculator
Insert any number or operation(+, -, *, /)""")
while(True):
	insert = input("")
	if(insert == "+"):
		check_stack(lists, add)
	elif(insert == "-"):
		check_stack(lists, minus)
	elif(insert == "*"):
		check_stack(lists, multiply)
	elif(insert == "/"):
		check_stack(lists, divide)
	elif(insert.isdigit()==True):
		push(lists, int(insert))
	elif(insert == "display"):
		for i in lists:
			print(i, end=", ")
		print("")
	elif(insert == "end"):
		break
	elif(insert == "erase"):
		delete_stack(lists)
	else:
		print("Input is not an integer or operation")