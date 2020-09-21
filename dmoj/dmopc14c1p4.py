import datetime

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
distance = abs(x2 - x1) + abs(y2 - y1)

start_time = datetime.datetime.strptime(input().strip(), "%Y:%m:%d:%H:%M:%S")
finish_time = start_time + datetime.timedelta(seconds = distance)
print(datetime.datetime.strftime(finish_time, "%Y:%m:%d:%H:%M:%S"))