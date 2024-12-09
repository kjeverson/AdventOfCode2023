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
freq_count = []
total = 0

# Build initial frequency count
freq_count = [1] * (len(lines))

for index in range(len(lines)):
	win_count = numberOfMatches(lines[index])
	for i in range(1, win_count+1):
		freq_count[index+i] = (freq_count[index+i] + freq_count[index]) 

print(sum(freq_count))
