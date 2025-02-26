N = int(input())
S = list(map(int, input().split()))

def max_milk(shops):
	cnt = 0
	next_milk = 0

	for shop in shops:
		if shop == next_milk:
			cnt += 1
			next_milk = (next_milk + 1) % 3

	return cnt

print(max_milk(S))