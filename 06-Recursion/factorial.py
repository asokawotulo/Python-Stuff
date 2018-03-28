def myfactorial(x):
	if(x == 1):
		return 1
	else:
		return x * myfactorial(x-1)

print(myfactorial(int(input("Input Number: "))))