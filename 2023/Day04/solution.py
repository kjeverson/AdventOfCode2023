import re

def readFile(filename):
	with open(filename, "r") as file:
		lines = file.readlines()
	
	return [line.strip("\n") for line in lines]

def numberOfMatches(line):
	win_numbers, your_numbers = line.split("|")

	win_numbers = re.sub(" +", " ", win_numbers)
	win_numbers = win_numbers.strip().split(" ")[2:]
	win_numbers = [int(number) for number in win_numbers]

	your_numbers = re.sub(" +", " ", your_numbers)
	your_numbers = your_numbers.strip(" ").split(" ")
	your_numbers = [int(number) for number in your_numbers]
	
	return len(set(win_numbers) & set(your_numbers))

lines = readFile("input")
total = 0
for line in lines:
	count = numberOfMatches(line)
	if count >= 1:
		count = count - 1
		total = total + pow(2, count)

print(total)
