import sys
input = sys.stdin.readline
n, d = input().split()
n, d = int(n), int(d)
intervals = input().split()
intervals = [int(i) for i in intervals]
val = 10000

for i in range(0, n):
    if d % intervals[i] == 0 and (d/intervals[i]) < val:
        val = int(abs(d/intervals[i]))
if val != 10000:
    print(val)
else:
    print('This is not the best time for a trip.')