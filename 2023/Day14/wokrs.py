def readFile(filename):
	with open(filename, "r") as file:
		lines = file.readlines()

	return [line.strip("\n") for line in lines]

def rotateMatrix(lines):
	return list(map(list, zip(*lines[::-1])))

def tilt(line):
	for i in range(len(line)-1, -1, -1):
		if line[i] == "O":
			j = i + 1
			while j < len(line) and line[j] != "O" and line[j] != "#":
				j = j + 1
			if i != j-1:
				line[j-1] = "O"
				line[i] = "."
		i = i - 1
	return line

def calcLoad(line):
	total = 0
	for i in range(len(line)):
		if line[i] == "O":
			total = total + (i + 1)

	return total

lines = readFile("test_input")
lines = rotateMatrix(lines)
total = 0
for line in lines:
	line = tilt(line)
	total = total + calcLoad(line)

print(total)
