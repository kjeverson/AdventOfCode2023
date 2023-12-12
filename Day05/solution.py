def readLines(filename):
	with open(filename, "r") as file:
		lines = file.read().split("\n\n")	

	return lines

def getSeeds(line):
	seeds = line.split(" ")[1:]
	return [int(seed) for seed in seeds]

def buildAlmanac(lines):
	almanac = []
	for line in lines:
		value_list = []
		values = line.splitlines()[1:]
		for value_set in values:
			value_set = value_set.split(" ")
			value_set = [int(value) for value in value_set]
			value_list.append(value_set)
			
		almanac.append(value_list)

	return almanac

def getNewSeed(seed, almanac):
	for part in almanac:
		if seed in range(part[1], part[1]+part[2]):
			diff = seed - part[1]
			seed = part[0] + diff
			break

	return seed

def getLocations(seeds, almanac_sections):
	locations = []
	for seed in seeds:
		for almanac in almanac_sections:
			seed = getNewSeed(seed, almanac)			
		locations.append(seed)

	return locations


lines = readLines("test_input")
seeds = getSeeds(lines.pop(0))
almanac_sections = buildAlmanac(lines)

locations = getLocations(seeds, almanac_sections)

print(locations)
print(min(locations))
