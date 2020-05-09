input = []
with open("test1.txt", "r") as f:
	for i,line in enumerate(f):
		input.append(list(line.strip()))

for row in input:
	for pixel in row:
		if pixel == "#":
			print("found one")


print(input)

