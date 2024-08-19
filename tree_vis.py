import pygame as pg
import random
import math

# data
data = []
start = random.randint(1, 100)

# window setup
WIDTH = 1280
HEIGHT = 720
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Collatz Conjecture - Visualised | Ben Collingridge")
clock = pg.time.Clock()
running = True

def collatz(n):
	if n % 2 == 0:
		return n / 2
	else:
		return (n * 3) + 1

def get_new_pos(h):
	vertical = h * math.sin(90) * 10
	horizontal = h * math.cos(90) * 10
	return pg.Vector2(horizontal, vertical)

n = start
i = 0
while n != 1:
	i += 1
	n = int(collatz(n))
	data.append(pg.Vector2(i, n))

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

	screen.fill("black")

	# --- LOGIC --- #



	#################

	# --- RENDER --- #

	for val in data:
		pg.draw.line(screen, "white", val, get_new_pos(val.x), 1)

	##################

	pg.display.update()
	pg.display.flip()
	clock.tick(144)

pg.quit()