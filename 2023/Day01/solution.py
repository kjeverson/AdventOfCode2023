def findFirstNumber(line):
	for char in line:
		if char.isdigit():
			return char

def findLastNumber(line):
	for char in line[::-1]:
		if char.isdigit():
			return char

lines = []
f = open("input", "r")

lines = f.readlines()
lines = [line.strip('\n') for line in lines]

total = 0

for line in lines:
	fNum = findFirstNumber(line)
	lNum = findLastNumber(line)
	tot = (int(fNum)*10) + int(lNum)
	total = total + tot

print(total)
