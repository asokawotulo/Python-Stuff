list = []
N = int(input())
for _ in range(N):
	command = input().split()
	func = command[0]
	if(func == "insert"):
		list.insert(int(command[1]), int(command[2]))
	elif(func == "print"):
		print(list)
	elif(func == "remove"):
		list.remove(int(command[1]))
	elif(func == "append"):
		list.append(int(command[1]))
	elif(func == "sort"):
		list.sort()
	elif(func == "pop"):
		list.pop()
	elif(func == "reverse"):
		list.reverse()