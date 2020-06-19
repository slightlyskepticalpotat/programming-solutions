import sys
input = sys.stdin.readline
reet = []

for i in range(0,4):
    reet.append(int(input().strip()))

reet.sort()

print(reet[0])
print(reet[3])