import sys
from itertools import combinations

input = sys.stdin.readline
e, s, m = map(int, input().rstrip().split())
year = 1

while True:
	if (year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
		break

	year += 1

print(year)

