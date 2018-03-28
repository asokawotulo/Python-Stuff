word = input()
word_s = word.split("*")
word_j = "".join(word_s)
word_l = list(word_j)

expressions = ["and", "attend", "append"]

for j in expressions:
	tf_result = []
	tf_result_2 = []
	for i in word_l:
		word_index = word.index(i)
		try:
			tf_result.append(i in j[word_index])
		except:
			tf_result.append(False)
			continue

	for k in word_s:
		tf_result_2.append(k in j)

	#if (False not in tf_result and False not in tf_result_2):
	if(False not in tf_result or False not in tf_result_2):
		print(j)