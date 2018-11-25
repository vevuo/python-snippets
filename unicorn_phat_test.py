# -*- coding: utf-8 -*-

from random import randint
from time import sleep
import datetime

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
		self.x = randint(0, 3)
		self.y = randint(0, 7)
		self.starttime = datetime.datetime.now()

def manage_lights():
	for light in lights:
		time_passed = datetime.datetime.now() - light.starttime
		if time_passed > datetime.timedelta(seconds=5):
			grid[light.x][light.y] = 0
			lights.remove(light)
		else:
			print(str(light.x) + " " + str(light.y))
			grid[light.x][light.y] = 1		

def draw():
	for row in grid:
		print(row)
	print("\n")

while True:
	#print(width, height)
	lights.append(Light())
	manage_lights()
	draw()
	sleep(0.5)