# -*- coding: utf-8 -*-

from random import randint
import time

grid = [
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0]
]

width = len(grid[0])
height = len(grid)

lights = []

class Light():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.starttime = time.time()

def manage_lights():
	for light in lights:
		if(time.time() - light.starttime >)
		grid[light.y][light.x] = 1


def draw():
	for row in grid:
		print(row)

while True:
	print(width, height)
	lights.append(Light())
	manage_lights()
	draw()
	sleep(0.5)