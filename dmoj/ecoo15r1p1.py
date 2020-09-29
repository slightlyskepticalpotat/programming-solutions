import math, sys

input = sys.stdin.readline

for i in range(10):
    smarties, total = [], 0
    while True:
        smartie = input().strip()
        if smartie == "end of box":
            break
        else:
            smarties.append(smartie)
    total += math.ceil(smarties.count("orange") / 7) * 13
    total += math.ceil(smarties.count("blue") / 7) * 13
    total += math.ceil(smarties.count("green") / 7) * 13
    total += math.ceil(smarties.count("yellow") / 7) * 13
    total += math.ceil(smarties.count("pink") / 7) * 13
    total += math.ceil(smarties.count("violet") / 7) * 13
    total += math.ceil(smarties.count("brown") / 7) * 13
    total += math.ceil(smarties.count("red")) * 16
    print(total)