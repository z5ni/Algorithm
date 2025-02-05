S1, S2, S3 = map(int, input().split())
s1 = list(range(1, S1+1))
s2 = list(range(1, S2+1))
s3 = list(range(1, S3+1))
dic = dict()

for s_1 in s1:
	for s_2 in s2:
		for s_3 in s3:
			s = s_1 + s_2 + s_3
			if s in dic.keys():
				dic[s] += dic.get(s, 0)
			else:
				dic[s] = 1

a = sorted(dic.items(), key=lambda x: -x[1])
print(a[0][0])

