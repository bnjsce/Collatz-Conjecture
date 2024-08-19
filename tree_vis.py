import pygame as pg
import random
import math

# data
data = []
runs = 6
# runs is the number of times it will make a chain from a random number until it converges to 1

# window setup
WIDTH = 1280
HEIGHT = 720
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Collatz Conjecture - Visualised | Ben Collingridge")
clock = pg.time.Clock()
running = True

def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False

def collatz(n):
	if is_even(n):
		return n / 2
	else:
		return (n * 3) + 1

# [origin, destination]
trunk = [pg.Vector2(screen.get_width() / 2, screen.get_height()), pg.Vector2(screen.get_width() / 2, screen.get_height() - 30)]
data.append(trunk)
for i in range(runs):
	n = random.randint(1, 150)
	i = 0
	while n != 1:
		i += 1
		n = int(collatz(n))
		mult = 0
		if is_even(n):
			mult = -1
		else:
			mult = 1
		data.append([data[i - 1][1], pg.Vector2(data[i - 1][1].x + mult * n, data[i - 1][1].y - 30)])

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

	screen.fill("black")

	# --- LOGIC --- #

	for val in data:
		pg.draw.line(screen, "white", val[0], val[1], 2)

	#################

	# --- RENDER --- #


	##################

	pg.display.update()
	pg.display.flip()
	clock.tick(144)

pg.quit()