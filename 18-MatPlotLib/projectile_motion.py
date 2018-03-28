import matplotlib.pyplot as plt
import numpy as np
from math import *

def find_y(init_vel, time, angle):
	global gravity
	return (init_vel * time) * sin(radians(angle)) - (0.5 * gravity) * time ** 2

def find_x(init_vel, time, angle):
	return (init_vel * time) * cos(radians(angle))

# Default Numbers
gravity = 9.81

x_values = []
y_values = []

for i in range(int(input("How many projectiles? "))):
	
	init_velocity = int(input("Initial velocity of projectile {}: ".format(i + 1)))
	angle = int(input("Angle of projectile {}: ".format(i + 1)))
	
	for t in np.arange(0.0, 300, 0.01):
		x_value = find_x(init_velocity, t, angle)
		y_value = find_y(init_velocity, t, angle)
		
		if y_value >= 0:
			# Append values that are only over 0
			x_values.append(x_value)
			y_values.append(y_value)
	
	plt.plot(x_values, y_values)
	
	del x_values[0:]
	del y_values[0:]

plt.show()