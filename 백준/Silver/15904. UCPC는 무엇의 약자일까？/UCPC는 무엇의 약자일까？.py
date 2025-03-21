import sys
input = sys.stdin.readline
S = input().rstrip()

result = ''

for char in S:
    if result == '' and char == 'U':
        result += char
    elif result == 'U' and char == 'C':
        result += char
    elif result == 'UC' and char == 'P':
        result += char
    elif result == 'UCP' and char == 'C':
        result += char

# print(result)
if result == "UCPC":
	print("I love UCPC")
else:
	print("I hate UCPC")