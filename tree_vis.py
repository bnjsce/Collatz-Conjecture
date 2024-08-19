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
	vertical = h.x * math.sin(90)
	horizontal = h.y * math.cos(90)
	return pg.Vector2(horizontal, vertical) * 10

n = start
i = 0
while n != 1:
	i += 1
	n = int(collatz(n))
	data.append(pg.Vector2(i * 30, n * 30))

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

	screen.fill("black")

	# --- LOGIC --- #



	#################

	# --- RENDER --- #

	for i in range(len(data)):
		#pg.draw.line(screen, "white", data[i - 1], get_new_pos(data[i]), 2)
		#pg.draw.line(screen, "white", data[i - 1], data[i], 2)
		#pg.draw.line(screen, "white", pg.Vector2(screen.get_width() / 2, screen.get_height()) - data[i], data[i], 2)
		pg.draw.line(screen, "white", pg.Vector2(screen.get_width() / 2, screen.get_height()), data[i], 2)

	##################

	pg.display.update()
	pg.display.flip()
	clock.tick(144)

pg.quit()