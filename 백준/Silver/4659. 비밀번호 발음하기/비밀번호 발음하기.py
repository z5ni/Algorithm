import sys

input = sys.stdin.readline


def is_ok(S):
	aeiou = 'aeiou'

	one = any(s in aeiou for s in S)
	if not one:
		return False

	cnt = 1
	for i in range(1, len(S)):
		if (S[i] in aeiou) == (S[i - 1] in aeiou):
			cnt += 1

			if cnt == 3:
				return False
		
		elif (S[i] not in aeiou) == (S[i - 1] not in aeiou):
			cnt += 1

			if cnt == 3:
				return False
		
		else:
			cnt = 1

	for i in range(1, len(S)):
		if S[i] == S[i-1] and S[i] not in ['e', 'o']:
			return False
	return True


while True:
	S = input().rstrip()

	if S == "end":
		break
	
	if is_ok(S):
		print(f"<{S}> is acceptable.")
	else:
		print(f"<{S}> is not acceptable.")
