import datetime
input_time = input().strip()
if input_time == "17":
    input_time = "0017"
if len(input_time) == 4:
    hours, minutes = int(input_time[:2]), int(input_time[2:])
else:
    hours, minutes = int(input_time[:-2]), int(input_time[1:])
time = datetime.datetime(2020, 6, 16, hours, minutes)

victoria = time+datetime.timedelta(minutes=-180)
edmonton = time+datetime.timedelta(minutes=-120)
winnipeg = time+datetime.timedelta(minutes=-60)
toronto = time+datetime.timedelta(minutes=0)
halifax = time+datetime.timedelta(minutes=60)
st_johns = time+datetime.timedelta(minutes=90)
print(int(time.strftime("%-H%M")), "in Ottawa")
print(int(victoria.strftime("%-H%M")), "in Victoria")
print(int(edmonton.strftime("%-H%M")), "in Edmonton")
print(int(winnipeg.strftime("%-H%M")), "in Winnipeg")
print(int(toronto.strftime("%-H%M")), "in Toronto")
print(int(halifax.strftime("%-H%M")), "in Halifax")
print(int(st_johns.strftime("%-H%M")), "in St. John's")