n = int(input())
students = []

for _ in range(n):
	name = input()
	score = float(input())
	students.append([name, score])

sorted_list = sorted(students, key=lambda x: -x[1])

min_value = sorted_list[n-1][1]
sorted_list = [list for list in sorted_list if min_value != list[1]]

min_value_2 = sorted_list[len(sorted_list)-1][1]
final_list = sorted([list for list in sorted_list if min_value_2 == list[1]], key=lambda x: x[0])

for i in range(len(final_list)):
	print(final_list[i][0])