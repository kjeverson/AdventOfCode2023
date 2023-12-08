import re

def readFile(filename):
	with open(filename, "r") as file:
		lines = file.readlines()

	return [line.strip("\n") for line in lines]

def checkLine(lines, i, j, line_length, sameLine=False):
	
	numbers = []

	matches = re.finditer("(\d+)", lines[i])
	for match in matches:
		if sameLine:
			if j == match.start() - 1:
				numbers.append(match.group())
			if j == match.end():
				numbers.append(match.group())
		else:
			if j in range(match.start()-1, match.end()+1):
				numbers.append(match.group())	
	return numbers

def findDigits(lines, i, j, num_lines, line_length):
	
	numbers = []

	if i-1 >= 0:
		result = checkLine(lines, i-1, j, line_length)
		if result:
			numbers.extend(result)

	if i+1 < num_lines:
		result = checkLine(lines, i+1, j, line_length)
		if result:
			numbers.extend(result)

	result = checkLine(lines, i, j, line_length, sameLine=True)
	if result:
		numbers.extend(result)

	return numbers

lines = readFile("input")

num_lines = len(lines)
line_length = len(lines[0])

total = 0

for i in range(num_lines):
	for j in range(line_length):
		if lines[i][j] == "*":			
			numbers = findDigits(lines, i, j, num_lines, line_length)	
			if numbers and len(numbers) == 2:
				ratio = int(numbers[0]) * int(numbers[1])
				total = total + ratio
		j = j + 1
	i = i + 1
			
print(total)
	
