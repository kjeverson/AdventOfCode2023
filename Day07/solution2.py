from collections import Counter

class Hand:
	def __init__(self, cards, bid):
		self.cards = cards
		self.bid = int(bid)
		self.rank = 0
		self.joker_count = self.cards.count("J")
		self.high_count = 0
		self.sec_high_count = 0
				
		self.getFreqCounts()
		self.high_count = self.high_count + self.joker_count
		self.classify()

	def __repr__(self):
		return "{}".format(self.cards)

	def __lt__(self, other):
		if self.rank < other.rank:
			return True
		elif self.rank > other.rank:
			return False
		else:
			return HighCard(self, other)

	def __eq__(self, other):
		return self.cards == other.cards

	def getFreqCounts(self):
		WC = Counter(self.cards)
		for letter, count in WC.items():
			if letter == "J":
				continue
			if count == 5:
				self.high_count = 5
				self.sec_high_count = 0
			elif count == 4:
				self.high_count = 4
				self.sec_high_count = 1
			elif count == 3:
				if self.high_count < count:
					self.sec_high_count = self.high_count
					self.high_count = 3
			elif count ==	2:
				if self.high_count <= count:
					self.sec_high_count = self.high_count
					self.high_count = 2
				else:
					self.sec_high_count = 2
			else:
				if self.high_count < count:
					self.sec_high_count = self.high_count
					self.high_count = 1

	def classify(self):
		if self.high_count == 5:
			self.rank = 7
		elif self.high_count == 4:
			self.rank = 6
		elif self.high_count == 3 and self.sec_high_count == 2:
			self.rank = 5
		elif self.high_count == 3:
			self.rank = 4
		elif self.high_count == 2 and self.sec_high_count == 2:
			self.rank = 3
		elif self.high_count == 2:
			self.rank = 2
		else:
			self.rank = 1

def HighCard(s, other):
	high = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1", "J"]
	for i in range(len(s.cards)):
		if s.cards[i] != other.cards[i]:
			return high.index(s.cards[i]) > high.index(other.cards[i])
		continue
	return False

def readFile(filename):
	with open(filename, "r") as file:
		lines = file.readlines()

	return [line.strip() for line in lines]

def parseLines(lines):
	hands = []
	for line in lines:
		cards, bid = line.split(" ")
		hands.append(Hand(cards, bid))
	
	return hands

total = 0
lines = readFile("input")
hands = parseLines(lines)
hands.sort()
for i in range(len(hands)):
	total = total + ( (i+1) * hands[i].bid)
print(total)
