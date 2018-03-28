from pokemon import Pokemon

def command_list():
	print("""List of Commands
[1] Find Pokemon Location
[2] Move Pokemon
[3] Reset Pokemon Location
[4] Exit""")

def main():
	pikachu = Pokemon("Pikachu", "Electric", "Male", "52", "5")
	command_list()
	command = int(input("Insert Command: "))
	while(command != 4):
		if(command == 1):
			if(pikachu.getLocation() == [0, 0]):
				print("Pokemon is at origin")
			else:
				print(pikachu.getLocation())
		elif(command == 2):
			direction = input("Input Direction (N/E/S/W): ").upper()
			if(direction == "N"):
				distance = int(input("Number of Units: "))
				pikachu.changeLocation(0, distance)
			elif(direction == "E"):
				distance = int(input("Number of Units: "))
				pikachu.changeLocation(distance, 0)
			elif(direction == "W"):
				distance = int(input("Number of Units: "))
				pikachu.changeLocation((-distance), 0)
			elif(direction == "S"):
				distance = int(input("Number of Units: "))
				pikachu.changeLocation(0, (-distance))
			else:
				print("Error not a valid direction")
		elif(command == 3):
			pikachu.resetLocation()
		print()
		command_list()
		command = int(input("Insert Command: "))
	print("You left the Pokemon to die alone... How cruel of you")

main()