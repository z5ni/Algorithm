import sys

input = sys.stdin.readline
M = int(input().rstrip())
N = int(input().rstrip())
L = sorted(list(map(int, input().rstrip().split())))

left = 0
right = M - 1
cnt = 0

while True:
	if left >= right:
		break
	
	if N == L[left] + L[right]:
		cnt += 1
		left += 1
		right -= 1

	if N > L[left] + L[right]:
		left = left + 1

	if N < L[left] + L[right]:
		right -= 1

print(cnt)