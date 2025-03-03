import sys

input = sys.stdin.readline
N, M = map(int, input().split())
words = {}
for _ in range(N):
	w = input().rstrip()
	if len(w) >= M:
		words[w] = words.get(w, 0) + 1

result = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
[print(k) for k, v in result]

