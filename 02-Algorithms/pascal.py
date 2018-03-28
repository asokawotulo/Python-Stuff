def pascal(value):
	disp_list = []
	for x in range(1, value+1):
		disp_list.append(1)
		print(disp_list)
		temp_list = []
		temp_list.append(disp_list[0])
		for i in range(len(disp_list)-1):
			temp_list.append(disp_list[i] + disp_list[i + 1])
		disp_list = temp_list
def main():
	number = int(input("Insert number of rows: "))
	pascal(number)
main()