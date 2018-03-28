def factorial(value):
	n = value
	while n > 1:
		n = n - 1
		value = value * n
	print(value)
def main():
	number = int(input("Please insert a number to factorial: "))
	factorial(number)
main()