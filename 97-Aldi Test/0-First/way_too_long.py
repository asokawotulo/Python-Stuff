letters = int(input())
for i in range(letters):
	word = str(input())
	temp = []
	if(len(word) > 10):
		temp.append(word[0])
		temp.append(str(len(word)-2))
		temp.append(word[len(word)-1])
		print("".join(temp))
	else:
		print(word)