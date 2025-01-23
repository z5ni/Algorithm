from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
d = deque()
for i in range(N):
    command = input().split()
    if command[0] == "push_front":
        d.appendleft(int(command[1]))
    elif command[0] == "push_back":
        d.append(int(command[1]))
    elif command[0] == "pop_front":
        print(d.popleft() if d else -1)
    elif command[0] == "pop_back":
        print(d.pop() if d else -1)
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        print(0 if d else 1)
    elif command[0] == "front":
        print(d[0] if d else -1)
    elif command[0] == "back":
        print(d[-1] if d else -1)