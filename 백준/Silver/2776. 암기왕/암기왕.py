T = int(input())
for _ in range(T):
	N = int(input())
	note1 = list(map(int, input().split()))
	M = int(input())
	note2 = list(map(int, input().split()))
	note1_dict = {}

	for n1 in note1:
		note1_dict[n1] = 1

	for n2 in note2:
		print(note1_dict.get(n2) or 0)