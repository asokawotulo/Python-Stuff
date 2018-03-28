word = input()

if(word.isupper() == True):
	print(word.swapcase())
elif(word[0].islower() == True):
	if(word[1:len(word)].isupper() == True):
		print(word.title())
	elif(len(word) == 1):
		print(word.title())
	else:
		print(word)
else:
	print(word)