import matplotlib.pylab as plt
import random

def f(x):
	return x**2-3*x+4

# List variables
x_values = [i for i in range(0, 26)]
y_values = []
random_x = []
random_y = []

# Assign y-values and random x & y values
for x in x_values:
	y_values.append(f(x))

for i in range(4000):
	random_x.append(random.randint(0, 25))
	random_y.append(random.randint(0, 600))

# Set maximum axis
axes = plt.gca()
axes.set_xlim([0,25])
axes.set_ylim([0,600])

plots = 0
for i in range(len(random_x)):
	index_y = random_x[i]
	if random_y[index_y] < y_values[index_y]:
		plots += 1

answer = plots/4000 * (25 * 600)
print(answer)
# Plot values
plt.plot(random_x, random_y, "o", color="blue")
plt.plot(x_values, y_values, marker="o", color="red")

plt.show()