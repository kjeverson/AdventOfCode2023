from collections import Counter

class Hand:
	def __init__(self, cards, bid):
		self.cards = cards
		self.bid = int(bid)
		self.rank = 0
				
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

	def classify(self):
	#	A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
		WC = Counter(self.cards)
		for letter, count in WC.items():
			if count == 5:
				self.rank = 7
			if count == 4:
				self.rank = 6
			if count == 3:
				if self.rank:
					self.rank = 5
				else:
					self.rank = 4
			if count == 2:
				if self.rank:
					if self.rank == 2:
						self.rank = 3
					if self.rank == 4:
						self.rank = 5
				else:
					self.rank = 2

def HighCard(s, other):
	high = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
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
