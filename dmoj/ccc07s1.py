import sys, datetime
e = datetime.date(2007,2,27)
def diff_dates(date1, date2):
    return abs(date2-date1).days

for i in range(0,int(sys.stdin.readline())):
    a, b, c = sys.stdin.readline().strip().split(' ')
    a, b, c = int(a), int(b), int(c)
    d = datetime.date(a,b,c)
    if a == 1989 and b == 2 and c == 27:
        print('Yes')    
    elif diff_dates(d,e) > 6575:
        print('Yes')
    else:
        print('No')