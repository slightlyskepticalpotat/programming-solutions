import sys
input = sys.stdin.readline
amounts = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
for i in range(int(input())):
    x = int(input())-1
    amounts[x] = 0
amounts = [thing for thing in amounts if thing != 0]

if sum(amounts)/len(amounts) >= int(input()):
    print("no deal")
else:
    print("deal")