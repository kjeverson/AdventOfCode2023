def readFile(filename):
	with open(filename, "r") as file:
		lines = file.readlines()

	return [line.strip("\n") for line in lines]

def checkSymbol(lines, i, j, num_lines, line_length):
	symbols = ["@", "#", "$", "%", "&", "*", "-", "+", "=", "/"]
	

	if i-1 >= 0: 
		if j-1 >= 0:
			if lines[i-1][j-1] in symbols:
				return True
		if j+1 < line_length:
			if lines[i-1][j+1] in symbols:
				return True
		if lines[i-1][j] in symbols:
			return True

	if i+1 < num_lines:
		if j-1 >= 0:
			if lines[i+1][j-1] in symbols:
				return True
		if j+1 < line_length:
			if lines[i+1][j+1] in symbols:
				return True
		if lines[i+1][j] in symbols:
			return True
		
	if j-1 >= 0:
		if lines[i][j-1] in symbols:
			return True

	if j+1 < line_length:
		if lines[i][j+1] in symbols:
			return True

	return False

lines = readFile("input")

num_lines = len(lines)
line_length = len(lines[0])

number = "" 
symbols = ["@", "#", "$", "%", "&", "*", "-", "+", "=", "/"]
found_symbol = False

total = 0

for i in range(num_lines):
	for j in range(line_length):
		if lines[i][j].isdigit():
			number = number + lines[i][j]
			if not found_symbol:
				found_symbol = checkSymbol(lines, i, j, num_lines, line_length)
		else:
			if number:
				if found_symbol:
					total = total + int(number)
				
				number = ""
				found_symbol = False
		
		j = j + 1
	i = i + 1
			
print(total)
	
