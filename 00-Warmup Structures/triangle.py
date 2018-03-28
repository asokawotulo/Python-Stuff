x = 0
h = 10

for i in range(1, h + 1):
	if(i == h):
		print("*" * (i * 2 - 1))
	else:
		print(" " * (h - i - 1), "*" * (i * 2 - 1))