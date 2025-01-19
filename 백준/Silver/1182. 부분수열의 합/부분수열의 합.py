from itertools import combinations

N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

# 1~N개까지의 수열을 만들 수 있음
# 가능한 리스트 조합 다 만들어놓고 sum이 S와 같은 경우의 개수를 구하자?

all_list = []
for i in range(1, len(lst) + 1):
	all_list.extend(list(combinations(lst, i)))

for ls in all_list:
	if sum(ls) == S:
		cnt += 1

print(cnt)