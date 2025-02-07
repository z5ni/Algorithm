N, M = map(int, input().split())
books = list(map(int, input().split()))
plus_book = []
minus_book = []

for b in books:
	if b > 0:
		plus_book.append(b)
	else:
		minus_book.append(-b)

minus_book.sort(reverse=True)
plus_book.sort(reverse=True)

# 돌아오지 않아도 되니까 제일 큰 숫자 마지막에 빼기
print(2 * sum(plus_book[::M]) + 2 * sum(minus_book[::M]) - max(plus_book + minus_book))
