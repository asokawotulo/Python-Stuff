def print_formatted(number):
	for i in range(1, number + 1):
		print(str(i).rjust(5, " "), str("{0:o}".format(i)).rjust(5, " "), str("%x"%(i)).rjust(5, " "), str("{0:b}".format(i)).rjust(5, " "))

n = int(input())
print_formatted(n)