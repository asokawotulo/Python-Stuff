x = 0
h = 10

for i in range(1, h + 1):
	if(i > h/2): 
		print(" " * (i), "*" * (((h - i) * 2) - 1))
	else: 
		print(" " * (h - i), "*" * (i * 2 - 1))