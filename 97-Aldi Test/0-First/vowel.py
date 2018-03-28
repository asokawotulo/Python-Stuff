word = input()

word_list = list(word)
vowel = "A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"
for i in range(len(word)):
	if(word_list[i] in vowel):
		word_list[i] = ""
	elif(word_list[i] not in vowel):
		word_list[i] = "." + word_list[i]
		if(word_list[i].isupper()):
			word_list[i] = word_list[i].swapcase()

print("".join(word_list))