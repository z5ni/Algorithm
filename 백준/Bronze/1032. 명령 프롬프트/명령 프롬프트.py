N = int(input())
strings = list()
pattern = list()
for _ in range(N):
   n = input()
   strings.append(n)

for i in range(len(strings[0])):
   	if all(s[i] == strings[0][i] for s in strings):
   		pattern.append(strings[0][i])
   	else:
   		pattern.append('?')

print(''.join(pattern))