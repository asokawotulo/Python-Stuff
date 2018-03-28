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
		return oper(stack, num_1, num_2)

def delete_stack(stack):
	del stack[:]

def main(insert_list):
	result = []
	for insert in insert_list:
		if(insert == "+"):
			result.append(check_stack(lists, add))
		elif(insert == "-"):
			result.append(check_stack(lists, minus))
		elif(insert == "*"):
			result.append(check_stack(lists, multiply))
		elif(insert == "/"):
			result.append(check_stack(lists, divide))
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
	print("Result:", result[-1])

def convert(expression):
	expression_list = expression.split()
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	oper_list = ["+", "-", "*", "/"]
	operations = []
	result = []
	for i in expression_list:
		if(i.isdigit()):
			result.append(i)
		elif(i == "("):
			operations.append(i)
		elif(i == ")"):
			popped_item = operations.pop()
			while(popped_item != "("):
				result.append(popped_item)
				popped_item = operations.pop()
		elif(i in oper_list):
			while(not not operations and (prec[operations[0]] >= prec[i])):
				result.append(operations.pop())
			operations.append(i)
		else:
			result.append(i)
	while not not operations:
		result.append(operations.pop())
	print("Infix expression:", " ".join(expression_list))
	print("Postfix expression:", " ".join(result))
	return result

lists = []
file = open("file.txt", "r")
print("""RPN Calculator""")
main(convert(file.read()))
file.close()