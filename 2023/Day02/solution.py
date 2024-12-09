import re

def readFile():
	with open("input", "r") as file:
		lines = file.readlines()
	
	return [line.strip("\n") for line in lines]

def buildDict(lines):
	dic = {}
	for line in lines:
		sections = line.split(";")
		ID, section = sections.pop(0).split(":")
		sections.append(section)
		
		ID = int(re.search('\d+', ID).group(0))

		dic.update({ID: {"green": 0, "red": 0, "blue": 0}})
	
		i=0
		for section in sections:
			parseParts(section, dic,ID, i)
			i = i + 1

	return dic

def parseParts(section, dic, ID, iteration):
	parts = section.split(",")
	for part in parts:
		count, color = re.search('(\d+) (\w+)', part).groups()
		count = int(count)

		if(dic[ID].get(color) < count):
			dic[ID][color] = count 
	return dic 

def checkGames(defaultDic, dic):
	count = 0;
	for ID, max_count in dic.items():
		if max_count.get("green") > defaultDic.get("green"):
			continue
		if max_count.get("blue") > defaultDic.get("blue"):
			continue
		if max_count.get("red") > defaultDic.get("red"):
			continue

		count = count + ID
	
	return count	

defaultDic = {
	"red": 12,
	"green": 13 ,
	"blue": 14
}


lines = readFile()
dic = buildDict(lines)
count = checkGames(defaultDic, dic)
print(count)
