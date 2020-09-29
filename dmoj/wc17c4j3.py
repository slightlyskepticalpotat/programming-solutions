stones = ["Mind", "Power", "Reality", "Soul", "Space", "Time"]
for i in range(int(input())):
    stones.remove(input().strip())
for stone in stones:
    print(stone)