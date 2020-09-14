import sys

input = sys.stdin.readline

motels, ways = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000], [1] + [0] * 7000 # 1 way to get to 0
a, b = int(input()), int(input())
for i in range(int(input())):
    motels.append(int(input()))
motels = [True if i in motels else False for i in range(7001)]

for i in range(7001):
    if motels[i]:
        for j in range(max(i - b, 0), i - a + 1): # how many ways are there to get here from the previous night?
            if motels[j]:
                ways[i] += ways[j] # work backwards one motel at a time
print(ways[7000])