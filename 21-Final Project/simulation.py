from pendulum import Pendulum
from numpy import sin, cos, arange
from matplotlib import pylab
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.integrate as integrate

# Physics Constants
gravity = 100

# User Input Constants for Pendulum
pendulum = Pendulum()

# Pendulum Length
length_one = pendulum.get_length_one()
length_two = pendulum.get_length_two()

# Pendulum Mass
mass_one = pendulum.get_mass_one()
mass_two = pendulum.get_mass_two()

# Pendulum Initial State
state = pendulum.get_state()

# Visible Objects
pendulum_visible = input("Would you like to see the Pendulum? (y/n) ")
trailing = input("Would you like to see the trail of the 2nd Pendulum? (y/n) ")
if trailing == "y":
	all_trail = input("Would you like to see the entire trail of the 2nd Pendulum? (y/n) ")

# Derivative function
def dydx(state, time):
	angle_one = state[0]
	omega_one = state[1]
	angle_two = state[2]
	omega_two = state[3]

	# Derivative of angle
	angle_one_der = omega_one
	angle_two_der = omega_two

	angle_diff = angle_one - angle_two
	mass_sum = mass_one + mass_two
	division_one = length_one*(mass_sum) - mass_two*length_one*cos(angle_diff)**2
	division_two = length_two*(mass_sum) - mass_two*length_two*cos(angle_diff)**2

	# Derivative of angular velocity
	omega_one_der = (-mass_two*length_one*angle_one_der**2*sin(angle_diff)*cos(angle_diff) + gravity*mass_two*sin(angle_two)*cos(angle_diff) - mass_two*length_two*angle_two_der**2*sin(angle_diff) - (mass_sum)*gravity*sin(angle_one))/division_one
	omega_two_der = (mass_two*length_two*angle_two_der**2*sin(angle_diff)*cos(angle_diff) + gravity*sin(angle_one)*cos(angle_diff)*(mass_sum) + length_one*angle_one_der**2*sin(angle_diff)*(mass_sum) - gravity*sin(angle_two)*(mass_sum))/division_two

	return [angle_one_der, omega_one_der, angle_two_der, omega_two_der]

# Time Constants
start_time = 0.0
total_time = float(input("Insert total time: ")) # Total time (s)
incre_time = 0.01 # Increment Time (s)
array_time = arange(start_time, total_time, incre_time)

# Grid and axis
max_space = length_one + length_two + 0.5
fig = plt.figure(facecolor="#000000")
fig.canvas.set_window_title('Double Pendulum')
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-max_space, max_space), ylim=(-max_space, max_space))
ax.text(0.01, max_space, "D O U B L E   P E N D U L U M", ha="left", color="white", fontsize=12)

# Time Template
time_template = 'Time = %.2fs'
time_text = ax.text(0.01, 0.925, '', transform=ax.transAxes, color="white")

# Pendulum Visible
if pendulum_visible.lower() == "y":
	line, = ax.plot([], [], 'o-', lw=2, color="#A15635", zorder=1)
	trace, = ax.plot([], [], '-', lw=1, color="#BCD4E6", zorder=0)
else:
	line, = ax.plot([], [], 'o-', lw=2, color="#000000", zorder=0)
	trace, = ax.plot([], [], '-', lw=1, color="#BCD4E6", zorder=1)

# Integrate differential equation
integration = integrate.odeint(dydx, state, array_time)

# Find xy positions of Pendulum 1 & 2
x_one =  length_one*sin(integration[:, 0])
x_two =  length_two*sin(integration[:, 2]) + x_one
y_one = -length_one*cos(integration[:, 0])
y_two = -length_two*cos(integration[:, 2]) + y_one

# Initial plot
def init():
	line.set_data([], [])
	time_text.set_text('')
	return line, time_text

# Animate
def animate(i):
	thisx = [0, x_one[i], x_two[i]]
	thisy = [0, y_one[i], y_two[i]]

	# Trailing 
	if trailing == "y" and all_trail == "n":
		if i - 400 < 0:
			trail = 0
		else:
			trail = i-400
		trace.set_data(x_two[trail:i], y_two[trail:i])
	elif trailing == "y":
		trace.set_data(x_two[:i], y_two[:i])

	# Plot xy
	line.set_data(thisx, thisy)

	# Display Time
	time_text.set_text(time_template % (i*incre_time + incre_time))
	return line, time_text

# Animate Function
ani = animation.FuncAnimation(fig, animate, arange(1, len(integration)), interval=5, init_func=init, repeat=False)

# Turn Axis Off & Show Plot
plt.axis("off")
plt.show()