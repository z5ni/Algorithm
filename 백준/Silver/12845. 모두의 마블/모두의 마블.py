n = int(input())
cards = list(map(int, input().split()))
cards.sort(reverse=True)

result = len(cards[1:])* cards[0] + sum(cards[1:])
print(result)