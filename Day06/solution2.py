import re


def readFile(filename):
	clean_lines = []
	with open(filename, "r") as file:
		lines = file.readlines()

	return [re.sub(" +", " ", line.strip("\n")) for line in lines]

def parseLines(lines):
	times = "".join(lines[0].split(" ")[1:])
	distances = "".join(lines[1].split(" ")[1:])

	return int(times), int(distances)


lines = readFile("input")
time, distance = parseLines(lines)

win = []
#results = 1
for i in range(1, time):
	if (time - i)* i > distance:
		win.append(i)

print(len(win))
