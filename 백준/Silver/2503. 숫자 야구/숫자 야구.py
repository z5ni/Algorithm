N = int(input())
# A - 100의 자리, B - 10의 자리, C - 1의 자리 서로 다른 숫자 세 개
# 모든 케이스를 통과하는 ABC의 개수를 세면 됨
tests = []

for _ in range(N):
	num, strike, ball = map(int, input().split())
	tests.append((num, strike, ball))
maybe = []

for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			if a == b or b == c or c == a:
				continue

			# 세자리 숫자가 정해짐
			for test in tests:
				# abc와 test[0]의 관계가 strike, ball을 만족하는지 확인하는 로직 필요
				bal = 0
				strik = 0

				if str(test[0])[0] == str(a):
					strik += 1
				elif str(a) in str(test[0]):
					bal += 1

				if str(test[0])[1] == str(b):
					strik += 1
				elif str(b) in str(test[0]):
					bal += 1

				if str(test[0])[2] == str(c):
					strik += 1
				elif str(c) in str(test[0]):
					bal += 1

				if strik == test[1] and bal == test[2]:
					# 가능성 있는 숫자조합을 리스트에 삽입
					maybe.append(a * 100 + b * 10 + c * 1)

# maybe 안에서 개수가 N개인거 개수 찾기
maybe_set = set(maybe)
maybe_dict = {}

for ms in maybe:
	maybe_dict[ms] = maybe_dict.get(ms, 0) + 1

cnt = 0
for k, v in maybe_dict.items():
	if v == N:
		cnt += 1

print(cnt)