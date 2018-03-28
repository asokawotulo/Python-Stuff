def find_max(list):
	max_num = 0
	for i in list:
		if(max_num < i):
			max_num = i
	return max_num

int_list = [x for x in range(100)]
print(find_max(int_list))