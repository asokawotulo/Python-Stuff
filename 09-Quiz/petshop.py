from animals import *
import random

def available_commands():
	print("""1. View pets
2. Purchase pet
3. Ask for help
99. Leave the store
""")

def animals():
	print("""1. Dogs
2. Cats
3. Tarantulas
""")
	return int(input("Pick animal: "))

def list_animals(list, command):
	if(command == "breed"):
		for i in range(len(list)):
			print(str(i+1) + ". " + list[i].get_breed())
	elif(command == "breed_price"):
		for i in range(len(list)):
			print(str(i+1) + ". " + list[i].get_breed_price())

def purchase(list, index):
	global purchased
	print("You just bought a " + list[index].get_breed())
	purchased.append(list[index])
	del list[index]

purchased = []
bought = []
dogs = [
animalia("Chihuahua", "$100", "1.5 Years", "Beige", "12-20 Years"), 
animalia("Siberian Husky", "$150", "0.5 Years", "White", "12-15 Years"),
animalia("Golden Retriever", "$75", "1 Years", "Gold", "10-12 Years"), 
animalia("Bulldog", "$25", "2 Years", "Brindle & White", "8-10 Years"), 
animalia("Shiba Inu", "$125", "1 Years", "Red Sesame", "12-15 Years"), 
animalia("Pug", "$100", "1.5 Years", "Fawn", "12-15 Years")
]
cats = [
animalia("British Shorthair", "$100", "1.5 Years", "Blue", "14-20 Years"), 
animalia("Siamese", "$150", "0.5 Years", "White", "15-20 Years"),
animalia("Persian", "$75", "1 Years", "Black", "15 Years"), 
animalia("Scotish Fold", "$25", "2 Years", "White", "15 Years")
]
tarantula = [
animalia("Chilean Rose", "$100", "Sling", "Red", "20-25(Female) Years, 15(Male) Years"), 
animalia("Mexican Redknee", "$150", "Sling", "White", "25-30(Female) Years, 10(Male) Years")
]

print("Welcome to the Pet Shop")
available_commands()
command = int(input("What would you like to do? "))
while(command != 99):
	if(command == 1):
		animal = animals()
		if(animal == 1):
			list_animals(dogs, "breed")
			more = input("Would you like to see more info? (Y/N) ").upper()
			if(more == "Y"):
				anim_index = int(input("Which would you like to see more? "))
				anim_indexes = anim_index - 1
				if(anim_indexes < 0):
					print("That is not within the given commands")
				else:
					dogs[anim_indexes].get_info()
					print()
		elif(animal == 2):
			list_animals(cats, "breed")
			more = input("Would you like to see more info? (Y/N) ").upper()
			if(more == "Y"):
				anim_index = int(input("Which would you like to see more? "))
				anim_indexes = anim_index - 1
				if(anim_indexes < 0):
					print("That is not within the given commands")
				else:
					cats[anim_indexes].get_info()
					print()
		elif(animal == 3):
			list_animals(tarantula, "breed")
			more = input("Would you like to see more info? (Y/N) ").upper()
			if(more == "Y"):
				anim_index = int(input("Which would you like to see more? "))
				anim_indexes = anim_index - 1
				if(anim_indexes < 0):
					print("That is not within the given commands")
				else:
					tarantula[anim_indexes].get_info()
					print()
	
	elif(command == 2):
		animal = animals()
		if(animal == 1):
			list_animals(dogs, "breed_price")
			anim_index = int(input("Which would you like to buy: "))
			anim_indexes = anim_index - 1
			if(anim_indexes < 0):
				print("That is not within the given commands")
			else:
				purchase(dogs, anim_indexes)
		elif(animal == 2):
			list_animals(cats, "breed_price")
			anim_index = int(input("Which would you like to buy: "))
			anim_indexes = anim_index - 1
			if(anim_indexes < 0):
				print("That is not within the given commands")
			else:
				purchase(cats, anim_indexes)
		elif(animal == 3):
			list_animals(tarantula, "breed_price")
			anim_index = int(input("Which would you like to buy: "))
			anim_indexes = anim_index - 1
			if(anim_indexes < 0):
				print("That is not within the given commands")
			else:
				purchase(tarantula, anim_indexes)
	
	elif(command == 3):
		available_commands()
	
	elif(command == 314):
		print("""1. Pet an animal
2. Steal an animal
99. Leave the store""")
		option = int(input("What would you like to do? "))
		chance = random.randint(0, 100)
		animal_option = animals()
		if(option == 1):
			if(animal_option == 1):
				if(chance <= 5):
					print("You tried to pet the Dog but it bit you :(")
					print("You ran away from the shop in pain\n")
					break
				else:
					print("You pet the dog :)")
			elif(animal_option == 2):
				if(chance <= 85):
					print("You tried to pet the Cat but it scratched you :(")
					print("You ran away from the shop in pain\n")
					break
				else:
					print("You pet the cat :)")
			elif(animal_option == 3):
				if(chance <= 25):
					print("You tried to pet the Tarantula but it bit you :(")
					print("You ran away from the shop in pain\n")
					break
				else:
					print("You pet the Tarantula :)")
		elif(option == 2):
			if(animal_option == 1):
				if(chance <= 5):
					print("You stole the dog :o. Such a bad boy")
					bought.append("Random Dog")
				else:
					print("You tried to steal the Dog but it bit you :(")
					print("You ran away from the shop in pain\n")
					break
			elif(animal_option == 2):
				if(chance <= 15):
					print("You stole the cat :o. Grumpy cat is grumpy")
					bought.append("Random Cat")
				else:
					print("You tried to steal the Cat but it scratched you :(")
					print("You ran away from the shop in pain\n")
					break
			elif(animal_option == 3):
				if(chance <= 35):
					print("You stole the tarantula :o. I dont have a tarantula pun...")
					bought.append("Random Tarantula")
				else:
					print("You tried to steal the tarantula but it bit you :(")
					print("You ran away from the shop in pain\n")
					break
	
	available_commands()
	command = int(input("What would you like to do? "))

total = 0
for i in purchased:
	total += int("".join(i.get_price().split("$")))
	bought.append(i.get_breed())
print("Pets recieved: " + ", ".join(bought))
print("Total amount spent: $" + str(total))
print("Thank you for visiting the Pet Shop")