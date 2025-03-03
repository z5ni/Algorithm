import sys

input = sys.stdin.readline
student = []
n = int(input())
for _ in range(n):
	name, d, m, y = map(str, input().rstrip().split())
	student.append((name, int(d), int(m), int(y)))

student = sorted(student, key=lambda x: (x[3], x[2], x[1]))
print(student[-1][0])
print(student[0][0])