start = int(input())
end = int(input())

for i in range(start,end+1):
    if (i - start) % 60 == 0:
        print('All positions change in year %s' % i)