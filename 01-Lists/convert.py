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
	print(" ".join(result))

convert("( 30 + 8 ) * 4")