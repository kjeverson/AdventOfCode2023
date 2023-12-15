def readFile(filename):
	with open(filename, "r") as file:
		lines = file.readlines()

	return [line.strip("\n") for line in lines]

def transposeMatrix(lines):
	return [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]

def tilt(line):
	new_line = line
	for i in range(len(line)):
		if line[i] == "O":
			j = i - 1
			while j >= 0 and line[j] != "O" and line[j] != "#":
				j = j - 1
			if i != j+1:
				line[j+1] = "O"
				line[i] = "."
	return line

def calcLoad(line):
	total = 0
	for i in range(len(line)):
		if line[i] == "O":
			total = total + (len(line) - i)

	return total

lines = readFile("input")
lines = transposeMatrix(lines)
total = 0
for line in lines:
	line = tilt(line)
	total = total + calcLoad(line)

print(total)
