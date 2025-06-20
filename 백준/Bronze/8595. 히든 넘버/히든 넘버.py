import sys
import re

input = sys.stdin.readline
n = int(input().rstrip())
s = input().rstrip()

s = re.sub("[a-zA-z]", ' ', s)
s = list(map(int, s.split()))

print(sum(s))