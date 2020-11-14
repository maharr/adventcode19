import numpy as np
from numpy import unravel_index
import math
input = []
asteroid = []
from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./input.txt")

with open(file_path, "r") as f:
	for i,line in enumerate(f):
		input.append(list(line.strip()))

for y,row in enumerate(input):
	for x,column in enumerate(row):
		if column == '#':
			asteroid.append([x,y])

count = {}
for station in asteroid:
	observation = []
	for target in asteroid:
		if target != station:
			observation.append(math.atan2(target[1]-station[1],target[0]-station[0]))
	observation = list(dict.fromkeys(observation))
	input[station[1]][station[0]] = len(observation)

print(input)

max = [0,0,0]
for y,row in enumerate(input):
	for x,column in enumerate(row):
		try:
			if column > max[0]:
				max = [column, x, y]
				print(max)
		except:
			pass