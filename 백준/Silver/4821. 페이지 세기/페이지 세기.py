

while True:
	cnt_page = int(input())
	
	if cnt_page == 0:
		break
	pages = set()
	hipen_pages = list(input().split(','))
	# print(hipen_pages)
	for p in hipen_pages:
		try:
			page = int(p)
			if 1 <= page <= cnt_page:
				pages.add(page)
		except:
			first, second = map(int, p.split('-'))
			if first <= second:
				for page in range(max(1, first), second+1):
					if page <= cnt_page:
						pages.add(page)

	print(len(pages))
