N = int(input())
# A - 100의 자리, B - 10의 자리, C - 1의 자리 서로 다른 숫자 세 개
# 모든 케이스를 통과하는 ABC의 개수를 세면 됨
tests = []

for _ in range(N):
	num, strike, ball = map(int, input().split())
	a_t = num // 100
	b_t = (num // 10) % 10
	c_t = num % 10

	tests.append((a_t, b_t, c_t, strike, ball))

cnt = 0
for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			if a == b or b == c or c == a:
				continue

			test_pass_cnt = 0

			for a_t, b_t, c_t, test_strike, test_ball in tests:
				strike = 0
				ball = 0

				# 숫자 계산이 문자열 계산보다 빠름
				if a == a_t:
					strike += 1
				elif a == b_t or a == c_t:
					ball += 1
				if b == b_t:
					strike += 1
				elif b == a_t or b == c_t:
					ball += 1
				if c == c_t:
					strike += 1
				elif c == b_t or c == a_t:
					ball += 1

				if strike == test_strike and ball == test_ball:
					test_pass_cnt += 1

			# 특정 숫자가 모든 테스트를 통과했을 경우에, 
			# 테스트 통과 카운트가 질문의 개수와 같음
			if test_pass_cnt == N:
				cnt += 1

print(cnt)
