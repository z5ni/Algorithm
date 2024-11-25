N = int(input())
card = dict()

for i in range(N):
	n = int(input())
	if card.get(n):
		card[n] += 1
	else:
		card[n] = 1

sorted_card = sorted(card.items(), key=lambda x: (-x[1], x[0]))
print(sorted_card[0][0])