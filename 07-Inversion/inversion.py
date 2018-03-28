file_name = str(input())

original = open(file_name + ".pgm", "br")
inverted = open(file_name + "inverted.pgm", "bw")

original_content = list(original.read())

for i in range(16, len(original_content)):
	original_content[i] = 255 - original_content[i]

inverted.write(bytes(original_content))

original.close()
inverted.close()