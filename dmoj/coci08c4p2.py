import datetime

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
d, m = map(int, input().split())
print(days[datetime.datetime(2009, m, d).weekday()])