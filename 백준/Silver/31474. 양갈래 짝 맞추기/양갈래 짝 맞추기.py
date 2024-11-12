N = int(input())    # 총 인원수
M = N // 2          # 테이블 수

n = 1   # 분자 (N!)
m = 1   # 분모 (M! * 2^M)

# N!을 구하기
for i in range(N, 0, -1):
    n *= i

# M!과 2^M을 구하기
for i in range(M):
    m *= (i + 1)    # M! 구하기
    m *= 2          # 2^M 구하기 

print(n // m)