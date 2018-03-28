def seperate(string):
	return string.split("-")

def main():
	acronym = []
	name = seperate(input())
	
	for part in name:
		acronym.append(part[0])

	print("".join(acronym))

main()