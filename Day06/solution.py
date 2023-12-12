import re


def readFile(filename):
	with open(filename, "r") as file:
		lines = file.readlines()

	return [re.sub(" +", " ", line.strip("\n")) for line in lines]

def parseLines(lines):

	return [int(line) for line in lines[0].split(" ")[1:]], [int(line) for line in lines[1].split(" ")[1:]]


lines = readFile("input")
times, distances = parseLines(lines)

results = 1
for i in range(len(times)):
	count = 0
	possible = list(range(1, times[i]))
	for p in possible:
		if (times[i] - p)*p > distances[i]:
			count = count + 1
	results = results * count

print(results)
