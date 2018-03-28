def evenodd(n):
	if(n % 2 == 0):
		return "Bob"
	else:
		return "Alice"

def main():
	stones = int(input())
	print(evenodd(stones))

main()