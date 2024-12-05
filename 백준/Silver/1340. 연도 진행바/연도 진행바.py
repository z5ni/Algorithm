from datetime import datetime, timedelta

now = input()
now_dt = datetime.strptime(now, "%B %d, %Y %H:%M")
year_start = datetime(now_dt.year, 1, 1, 0, 0)

total_days = 366 if (now_dt.year % 400 == 0 or (now_dt.year % 4 == 0 and now_dt.year % 100 != 0)) else 365
minutes_passed = (now_dt - year_start).total_seconds() / 60

progress = (minutes_passed / (total_days * 24 * 60)) * 100
print(progress)