N = int(input())
# A - 100의 자리, B - 10의 자리, C - 1의 자리 서로 다른 숫자 세 개
# 모든 케이스를 통과하는 ABC의 개수를 세면 됨
tests = []

for _ in range(N):
	num, strike, ball = map(int, input().split())
	tests.append((num, strike, ball))

cnt = 0
for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			if a == b or b == c or c == a:
				continue

			current = f"{a}{b}{c}"
			test_pass_cnt = 0

			for test_num, test_strike, test_ball in tests:
				strike = 0
				ball = 0

				# 인덱스로 비교
				for i in range(3):
					if current[i] == str(test_num)[i]:
						strike += 1
					elif current[i] in str(test_num):
						ball += 1
				# print(f"{current} {test_num} {strike} {ball}")

				if strike == test_strike and ball == test_ball:
					test_pass_cnt += 1

			# 특정 숫자가 모든 테스트를 통과했을 경우에, 
			# 테스트 통과 카운트가 질문의 개수와 같음
			if test_pass_cnt == N:
				cnt += 1

print(cnt)
