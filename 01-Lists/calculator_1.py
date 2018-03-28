def add(int_1, int_2, lists):
	lists.append(int_1)
	lists.append(int_2)
	num_1 = lists.pop()
	num_2 = lists.pop()
	result = num_1 + num_2
	lists.append(result)
	return result

stack = []
num_1 = int(input("First Number: "))
num_2 = int(input("Second Number: "))

print("Sum:", add(num_1, num_2, stack))