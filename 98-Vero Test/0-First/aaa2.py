word = input()
word_s = word.split("*")
word_j = "".join(word)
word_l = list(word_j)
expressions = ["and", "attend", "append"]
verify = [False, False, False]

for i in range(len(expressions)):
	for j in range(len(word_s)):
		print(expressions[i][j])
		if(word_s[j] == expressions[i][0]):
			if (word_s[j] == expressions[i][-len(word_s[j]):]):
				print(expressions[i])