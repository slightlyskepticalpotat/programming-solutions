import datetime

date1 = datetime.datetime.strptime(input().strip(), "%Y/%m/%d")
date2 = datetime.datetime.strptime(input().strip(), "%Y/%m/%d")
print(int((date2 - date1).total_seconds()/86400)) # seconds in day