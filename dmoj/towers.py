towers = int(input())
map = [int(i) for i in input().split()]
good = 0

for i in range(1, len(map)-1):
    if map[i-1] < map[i] < map[i+1]:
        good+=1
print(good)