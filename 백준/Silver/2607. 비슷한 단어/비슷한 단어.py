import sys
input = sys.stdin.readline
n = int(input().rstrip())
S = input().rstrip()

S_dict = {}
for char in S:
    S_dict[char] = S_dict.get(char, 0) + 1
cnt = 0

for _ in range(n-1):
    T = input().rstrip()
    T_dict = {}
    for char in T:
        T_dict[char] = T_dict.get(char, 0) + 1
    
    if S_dict == T_dict:
        cnt += 1
        continue
    
    if abs(len(S) - len(T)) > 1:
        continue
    
    if len(T) == len(S) + 1:
        for char in T:
            if T_dict[char] > 0:
                temp = T_dict.copy()
                temp[char] -= 1
                if temp[char] == 0:
                    del temp[char]
                if temp == S_dict:
                    cnt += 1
                    break

    elif len(S) == len(T) + 1:
        for char in S:
            if S_dict[char] > 0:
                temp = S_dict.copy()
                temp[char] -= 1
                if temp[char] == 0:
                    del temp[char]
                if temp == T_dict:
                    cnt += 1
                    break
    
    elif len(S) == len(T):
        diff = 0
        for char in set(list(S) + list(T)):
            diff += abs(S_dict.get(char, 0) - T_dict.get(char, 0))
        if diff == 2:
            cnt += 1
            
print(cnt)