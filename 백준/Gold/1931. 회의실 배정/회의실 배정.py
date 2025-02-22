N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst = sorted(lst, key=lambda x: (x[1], x[0]))
cnt = 1
end_time = lst[0][1]

for start, end in lst[1:]:
	if start >= end_time:
		cnt += 1
		end_time = end

print(cnt)
