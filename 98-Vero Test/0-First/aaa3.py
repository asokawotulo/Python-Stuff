word = input()
word_s = word.split("*")

expressions = ["and", "attend", "append"]
counter = 0

for j in expressions:
	tf_result = []
	for i in word_s:
		tf_result.append(i in j)
	if False not in tf_result:
		print(j)