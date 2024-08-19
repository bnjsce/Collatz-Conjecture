import random
import matplotlib.pyplot as plt

# even = n / 2
# odd = 3n + 1

# data
x = []
y = []
x2 = []
y2 = []
definite_steps = 200
start = random.randint(1, 100)

# if mode is d, run for a number of steps
# if mode is i, run until n becomes 1
# if mode is b, run both
mode = "b"

def collatz(n):
	if n % 2 == 0:
		return n / 2
	else:
		return (n * 3) + 1

def find_data_definite():
	n = start
	for i in range(1, definite_steps + 1):
		n = int(collatz(n))
		x.append(i)
		y.append(n)
	plot_data(x, y, "Collatz Conjecture - Visualised | Ben Collingridge", definite_steps, f"Steps (Definite) - Converged to {y[len(y) - 1]}", f"n - Start: {start}")

def find_data_indefinite():
	n = start
	i = 0
	while n != 1:
		i += 1
		n = int(collatz(n))
		x.append(i)
		y.append(n)
	plot_data(x, y, "Collatz Conjecture - Visualised | Ben Collingridge", i, "Steps (Indefinite)", f"n - Start: {start}")

def find_data_both():
	# definite
	n = start
	for i in range(1, definite_steps + 1):
		n = int(collatz(n))
		x.append(i)
		y.append(n)

	# indefinite
	n2 = start
	i2 = 0
	while n2 != 1:
		i2 += 1
		n2 = int(collatz(n2))
		x2.append(i2)
		y2.append(n2)

	plt.plot(x, y, marker="o", markerfacecolor="red", markersize=5, label="Definite")
	plt.plot(x2, y2, marker="o", markerfacecolor="green", markersize=5, label="Indefinite")
	plt.xlim(1, definite_steps)
	plt.ylim(1, max(y))
	plt.xlabel("Steps")
	plt.ylabel(f"n - Start: {start}")
	plt.title("Collatz Conjecture - Visualised | Ben Collingridge")
	plt.legend()
	plt.show()

def plot_data(x_data, y_data, plot_title, steps, x_label="X-axis", y_label="Y-axis"):
	plt.plot(x_data, y_data, marker="o", markerfacecolor="red", markersize=5)
	plt.xlim(1, steps)
	plt.ylim(1, max(y_data))
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(plot_title)
	plt.show()

if mode == "d":
	find_data_definite()
elif mode == "i":
	find_data_indefinite()
else:
	find_data_both()