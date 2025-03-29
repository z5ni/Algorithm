import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
circle = deque(range(1, N+1))
L = []

while circle:
	for _ in range(K-1):
		circle.append(circle.popleft())

	L.append(str(circle.popleft()))

print(f"<{', '.join(L)}>")