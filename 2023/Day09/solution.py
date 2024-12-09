def readFile(filename):
	with open(filename, "r") as file:
		lines = file.readlines()

	return [line.strip("\n") for line in lines]

def getNumbers(line):
	return [int(num) for num in line.split()]

def getDifferences(line):

	diff_list = []
	for i in range(len(line)):
		if i+1 >= len(line):
			continue
		else:
			diff_list.append(line[i+1] - line[i])
	
	return line[-1] + getDifferences(diff_list) if any(line) else 0


lines = readFile("input")
last = 0
for line in lines:
	line = getNumbers(line)
	last = last + getDifferences(line)

print(last)
