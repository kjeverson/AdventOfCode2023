def findNumber(line, reverse=False):
	if reverse:
		line = line[::-1]

	for i in range(len(line)):
		if line[i].isdigit():
			return i, int(line[i])
		i = i + 1

	return None, None

def findWord(line, reverse=False):

	words_for = {
		"one": 1, "two": 2, "three": 3, 
		"four": 4, "five": 5, "six": 6, 
		"seven": 7, "eight": 8, "nine": 9
	}
	words_rev = {
		"eno": 1, "owt": 2, "eerht": 3, 
		"ruof": 4, "evif": 5, "xis": 6, 
		"neves": 7, "thgie": 8, "enin": 9
	}

	index = None
	value = None
	
	if reverse is False:
		words = words_for.keys()
	else:
		words = words_rev.keys()
		line = line[::-1]

	for word in words:
		result = line.find(word)
		if index == None and result != -1:
			index = result
			value = word
		if result != -1 and result < index:
			index = result
			value = word
	
	if reverse and value:
		value = words_rev.get(value)
	if not reverse and value:
		value = words_for.get(value)
	
	return index, value

lines = []
f = open("input", "r")

lines = f.readlines()
lines = [line.strip('\n') for line in lines]

total = 0

for line in lines:
	fWordIndex, fWValue = findWord(line)
	lWordIndex, lWValue = findWord(line, reverse=True)
	fNumIndex, fNValue = findNumber(line)
	lNumIndex, lNValue = findNumber(line, reverse=True)

	if fWordIndex != None and fNumIndex != None:
		if fWordIndex < fNumIndex:
			fNum = fWValue * 10
		else:
			fNum = fNValue * 10
	else:
		if fWordIndex != None:
			fNum = fWValue * 10
		else:
			fNum = fNValue * 10


	if lWordIndex != None and lNumIndex != None:
		if lWordIndex < lNumIndex:
			lNum = lWValue
		else:
			lNum = lNValue
	else:
		if lWordIndex != None:
			lNum = lWValue
		else:
			lNum = lNValue
	
	tot = fNum + lNum
	total = total + tot

print(total)
