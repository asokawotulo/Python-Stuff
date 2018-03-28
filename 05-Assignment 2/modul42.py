def modul42(list):
	for i in range(10):
		value = int(input())
		list.append(value % 42)

def main():
	answer = []
	modul42(answer)
	print(len(set(answer)))

main()