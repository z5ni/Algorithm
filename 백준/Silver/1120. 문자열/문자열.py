import sys

input = sys.stdin.readline

A, B = map(str, input().rstrip().split())
max_cnt = 0
word = ''
idx = -1

for i in range(len(B) - len(A) + 1):
	cnt = 0
	b_copy = B[i:i+len(A)]
	for j in range(len(A)):
		if b_copy[j] == A[j]:
			cnt += 1
	max_cnt = max(max_cnt, cnt)
	
print(len(A) - max_cnt)

