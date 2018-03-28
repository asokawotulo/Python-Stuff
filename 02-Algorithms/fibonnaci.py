def fibonnaci(value):
	i = x = 0
	y = 1
	while i < value:
		if(i <= 1):
			result = i
		else:
			result = x + y
			x = y
			y = result
		print(result, end = ", ")
		i += 1
def main():
	number = int(input("Input nth term of Fibonnaci sequence: "))
	fibonnaci(number)
main()