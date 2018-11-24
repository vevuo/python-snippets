# -*- coding: utf-8 -*-

from random import randint
from time import sleep

grid = [
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0]
]

width = len(grid[0])
height = len(grid)

def draw():
	for row in grid:
		print(row)

while True:
	print(width, height)
	draw()
	sleep(0.5)