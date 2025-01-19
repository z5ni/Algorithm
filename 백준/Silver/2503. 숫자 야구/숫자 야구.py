from itertools import permutations

N = int(input())
questions = [input().split() for _ in range(N)]
cnt = 0

# 서로 다른 숫자 세 개로 이루어진 세 자리 수 -> 자리 상관 있음 => 순열
for p in permutations(range(1, 10), 3):
	# 만약 ok가 False가 될 경우 남은 경우의 수를 확인하지 않음
	ok = True

	for num, st, bl in questions:
		strike = ball = 0

		# 인덱스로 비교
		for i in range(3):
			if str(p[i]) == num[i]:
				strike += 1
			elif str(p[i]) in num:
				ball += 1

		if strike != int(st) or ball != int(bl):
			ok = False
			break

	if ok:
		cnt += 1

print(cnt)
