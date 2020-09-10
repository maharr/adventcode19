import numpy as np
input = []
asteroid = []
from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./test1.txt")

with open(file_path, "r") as f:
	for i,line in enumerate(f):
		input.append(list(line.strip()))

for y,row in enumerate(input):
	for x,column in enumerate(row):
		if column == '#':
			asteroid.append([x,y])

for station in asteroid:
	observation = []
	for target in asteroid:
		if target != station:
			
			print(target[1]-station[1]/target[0]-station[0])

			
print(asteroid)
print(np.matrix(input))
