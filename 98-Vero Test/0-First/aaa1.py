word = input().split("*")
word_j = "".join(word)
word_l = list(word_j)
expressions = ["and", "attend", "append"]
result = []

for i in range(len(expressions)):
	if(word[0] == expressions[i][0]):
		print(expressions[i][-len(word):len(expressions[i])])
		print(word[len(word_j[len(word_j)-1]):len(word)])
		for j in range(len(word)):
			if(expressions[i][-len(word):len(expressions[i])] in word[len(word_j[len(word_j)-1]):len(word)]):
				result.append(expressions[i])
print(result)