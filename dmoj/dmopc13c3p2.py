import datetime

s = int(input())
now = datetime.datetime.strptime(input().strip(), "%Y/%m/%d %H:%M:%S")
arrival = now - datetime.timedelta(hours=s)
print(datetime.datetime.strftime(arrival, "%Y/%m/%d %H:%M:%S"))