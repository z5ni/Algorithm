N = int(input())

cnt = 0
chatting = set()

for _ in range(N):
	chat = input()
	if chat == "ENTER":
		cnt += len(chatting)
		chatting = set()
	else:
		chatting.add(chat)

print(cnt + len(chatting))