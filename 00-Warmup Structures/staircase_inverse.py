x = 0
h = 10

for i in range(1, h + 1):
	if(i == h):
		print("*" * i)
	else:
		print(" " * (h - i - 1), "*" * i)