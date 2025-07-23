import sys
from itertools import permutations

input = sys.stdin.readline
k = int(input().rstrip())
mark = list(map(str, input().rstrip().split()))
pred1 = list(permutations(list(range(10)), k + 1))

flag = False
for pr in pred1[::-1]:
	cnt = 0

	for i in range(1, k+1):
		if mark[i-1] == "<" and pr[i-1] < pr[i]:
			cnt += 1

		if mark[i-1] == ">" and pr[i-1] > pr[i]:
			cnt += 1

		if cnt == k:
			flag = True
			print(''.join(map(str, pr)))

	if flag:
		break


flag = False

for pr in pred1:
	cnt = 0

	for i in range(1, k+1):
		if mark[i-1] == "<" and pr[i-1] < pr[i]:
			cnt += 1

		if mark[i-1] == ">" and pr[i-1] > pr[i]:
			cnt += 1

		if cnt == k:
			flag = True
			print(''.join(map(str, pr)))

	if flag:
		break
