x = int(input())
y = int(input())
z = int(input())
n = int(input())
list = []
counter = 0

for i in range(x + 1):
	for j in range(y + 1):
		for k in range(z + 1):
			if(i + j + k != n):
				list.append([])
				list[counter] = [i, j, k]
				counter += 1
print(list)