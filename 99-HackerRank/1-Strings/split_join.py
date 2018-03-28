def split_and_join(line):
	return line.replace(" ", "-")

line = input()
result = split_and_join(line)
print(result)