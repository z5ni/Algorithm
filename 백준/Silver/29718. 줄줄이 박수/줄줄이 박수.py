import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
rows = [0] * m

for _ in range(n):
	L = list(map(int, input().rstrip().split()))

	for i in range(m):
		rows[i] += L[i]

a = int(input().rstrip())

def slide_row(lst, a):
	result = 0
	
	for i in range(len(lst) - a + 1):
		if result < sum(lst[i:i + a]):
			result = sum(lst[i:i + a])
	return result

print(slide_row(rows, a))