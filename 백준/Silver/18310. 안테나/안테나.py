n = int(input())
houses = list(map(int, input().split()))
houses.sort()

prev = len(houses)//2-1
prev_value = houses[prev] * len(houses[:prev]) - sum(houses[:prev]) + sum(houses[prev:]) - houses[prev] * len(houses[prev:])

nex = len(houses)//2
nex_value = houses[nex] * len(houses[:nex]) - sum(houses[:nex]) + sum(houses[nex:]) - houses[nex] * len(houses[nex:])

print(houses[prev] if prev_value <= nex_value else houses[nex])
