N = int(input())
students = list()

for i in range(N):
	n = input()
	students.append(n)

for j in range(1, len(students[0])+1):
	result = list(map(lambda x: x[-j:], students))
	if len(result) == len(set(result)):
		print(j)
		break