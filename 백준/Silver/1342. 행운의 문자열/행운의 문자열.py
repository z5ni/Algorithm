S = list(input())

# 각 문자의 개수 count
# 이전 문자와 값이 같지 않을 경우만 판단
choose = []
cnt = dict()
set_S = set(S)
answer = 0

for s in S:
	cnt[s] = cnt.get(s, 0) + 1

# print(cnt)

def lucky(pick_cnt):
	global choose, S, set_S, cnt, answer
	
	# 재귀 조건이 모두 만족하는 문자열이 만들어진 경우
	if pick_cnt == len(S):
		# print(choose)
		answer += 1
		return
	# choose의 이전 문자 != 현재 넣으려하는 문자가 같지 않을 경우에만 choose에 넣기

	# 선택할 수 있는 문자의 개수가 남아있는지 확인
	for s in set_S:
		if cnt[s] == 0:
			continue

		if len(choose) == 0:
			cnt[s] -= 1
			choose.append(s)
			lucky(pick_cnt + 1)
			choose.pop()
			cnt[s] += 1
		elif choose[-1] != s:
			cnt[s] -= 1
			choose.append(s)
			lucky(pick_cnt + 1)
			choose.pop()
			cnt[s] += 1


lucky(0)
print(answer)
	
