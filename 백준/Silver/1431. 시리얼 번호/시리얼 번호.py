N = int(input())
gui = list()
gui_d = dict()

for i in range(N):
	n = input()
	gui.append(n)

for g in gui:
	a = [int(x) for x in g if x.isdigit()]
	gui_d[g] = sum(a)

A = sorted(gui_d.items(), key=lambda x: (len(x[0]), x[1], x[0]))

for a in A:
	print(a[0])