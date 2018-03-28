def calculate_velocity(init_v, accel, time):
	return init_v + (accel * time)

def distance_travelled(init_v, accel, time):
	return (init_v * time) + ((accel * 0.5) * (time ** 2))

def main(init_v, speed_limit):
	tot_time = int(input("Time spent on the road: "))
	accel = int(input("Acceleration: "))
	total_distance = int(input("Target distance: "))
	max_v = calculate_velocity(init_v, accel, tot_time)
	max_d = distance_travelled(init_v, accel, tot_time)

	for t in range(tot_time + 1):
		print("Duration:", t, "Distance", "*" * int(distance_travelled(init_v, accel, t) // 10))

	if(max_v > speed_limit):
		print("The driver went over the speed limit. (Max speed was", max_v, "m/s)")
	if(max_d >= total_distance):
		print("The person reached the destination. (Reached", max_d, "m)")
	if(max_v < speed_limit):
		print("The driver did not go over the speed limit. (Max speed was", max_v, "m/s)")
	if(max_d < total_distance):
		print("The person did not reach the destination. (Reached", max_d, "m)")

main(0, 60) 