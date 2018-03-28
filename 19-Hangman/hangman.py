import sys
def print_lives(lives):
	if(lives == 1):
		print("""





|----
""")
	elif(lives == 2):
		print("""
|
|
|
|
|
|----
""")
	elif(lives == 3):
		print("""
|----
|
|
|
|
|----
""")
	elif(lives == 4):
		print("""
|----
|   |
|
|
|
|----
""")
	elif(lives == 5):
		print("""
|----
|   |
|   O
|   
|
|----
""")
	elif(lives == 6):
		print("""
|----
|   |
|   O
|   |
|
|----
""")
	elif(lives == 7):
		print("""
|----
|   |
|  \O
|   |
|
|----""")
	elif(lives == 8):
		print("""
|----
|   |
|  \O/
|   |
|
|----""")
	elif(lives == 9):
		print("""
|----
|   |
|  \O/
|   |
|  / 
|----""")
	elif(lives == 10):
		print("""
|----
|   |
|  \O/
|   |
|  / \\
|----""")
		sys.exit()
word = list("fish sticks")
guessed_word = list("**** ******")
lives = 0
alp1 = 0
alp2 = 0
alp3 = 0
alp4 = 0
alp5 = 0
alp6 = 0
alp7 = 0

print("Hangman")

while(word != guessed_word):
	a = input()
	if(a == "f"):
		guessed_word[0] = "f"
		alp1 += 1
		if(alp1 <= 1):
			print("".join(guessed_word))
		else:
			lives += 1
			print_lives(lives)
	elif(a == "i"):
		guessed_word[1] = "i"
		guessed_word[7] = "i"
		alp2 += 1
		if(alp2 <= 1):
			print("".join(guessed_word))
		else:
			lives += 1
			print_lives(lives)
	elif(a == "s"):
		guessed_word[2] = "s"
		guessed_word[5] = "s"
		guessed_word[10] = "s"
		alp3 += 1
		if(alp3 <= 1):
			print("".join(guessed_word))
		else:
			lives += 1
			print_lives(lives)
	elif(a == "h"):
		guessed_word[3] = "h"
		alp4 += 1
		if(alp4 <= 1):
			print("".join(guessed_word))
		else:
			lives += 1
			print_lives(lives)
	elif(a == "t"):
		guessed_word[6] = "t"
		alp5 += 1
		if(alp5 <= 1):
			print("".join(guessed_word))
		else:
			lives += 1
			print_lives(lives)
	elif(a == "c"):
		guessed_word[8] = "c"
		alp6 += 1
		if(alp6 <= 1):
			print("".join(guessed_word))
		else:
			lives += 1
			print_lives(lives)
	elif(a == "k"):
		guessed_word[9] = "k"
		alp7 += 1
		if(alp7 <= 1):
			print("".join(guessed_word))
		else:
			lives += 1
			print_lives(lives)
	else:
		lives += 1
		print_lives(lives)