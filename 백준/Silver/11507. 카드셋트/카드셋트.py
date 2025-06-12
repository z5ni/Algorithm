import sys

input = sys.stdin.readline
S = input().rstrip()
l = [i * 3 for i in range(len(S)//3)]
cards = [S[i:i+3] for i in l]
poker = {"P": 13, "K": 13, "H": 13, "T": 13}

if len(cards) != len(set(cards)):
	print("GRESKA")
else:
	for card in cards:
		poker[card[0]] = poker.get(card[0]) - 1

	[print(v, end=' ') for v in poker.values()]
