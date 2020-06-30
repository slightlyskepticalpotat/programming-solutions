start, days = map(int, input().split())
calender = []
def pad(x):
    x = str(x)
    x = " "*(4-len(x)) + x
    return x
print("Sun Mon Tue Wed Thr Fri Sat")
for i in range(start-1):
    calender.append(pad(""))
for i in range(1, days+1):
    calender.append(pad(i))
for i in range(0, len(calender)):
    if i % 7 == 0 and i != 0:
        print("")
    if i % 7 == 0:
        print(calender[i][1:], end="")
    else:
        print(calender[i], end="")
print("")