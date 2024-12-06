from datetime import datetime

x, y = map(int, input().split())
dt = datetime(2007, x, y)

print(dt.strftime("%A")[:3].upper())