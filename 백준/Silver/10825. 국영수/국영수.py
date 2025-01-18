N = int(input())
student = []
for _ in range(N):
	name, k, e, m = map(str, input().split())
	student.append((name, int(k), int(e), int(m)))

student = sorted(student, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for n, _, _, _ in student:
	print(n)