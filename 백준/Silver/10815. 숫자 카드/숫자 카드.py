N = int(input())
num = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))
dic = {}

# * M, N 값이 큰 경우 dictionary를 이용 *
# dict는 해시 테이블(Hash Table) 구조를 사용해 키를 통한 값 접근 -> O(1)
# list는 값을 찾기 위해서 처음부터 순차적으로 탐색 -> O(M * N)

for n in num:
	dic[n] = 1

for c in card:
	print(dic.get(c) or 0, end=" ")