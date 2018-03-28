def case(condition, pos):
	if (condition == "A"):
		pos[0], pos[1] = pos[1], pos[0]
	elif (condition == "B"):
		pos[1], pos[2] = pos[2], pos[1]
	elif (condition == "C"):
		pos[0], pos[2] = pos[2], pos[0]

def main():
	ball = [1, 0, 0]
	for sequence in list(input()):
		case(sequence, ball)
	print(ball.index(1)+1)

main()