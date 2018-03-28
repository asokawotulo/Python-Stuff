n = int(input())

x = 0
for i in range(n):
	command = input()
	if ("++" in command):
		x += 1
	elif ("--" in command):
		x -= 1
print(x)