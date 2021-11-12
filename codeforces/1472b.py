for _ in range(int(input())):
    n = int(input())
    candies = [int(i) for i in input().split()]
    ones, twos = candies.count(1), candies.count(2)
    total = sum(candies) / 2
    flag = False
    for i in range(0, ones + 1):
        for j in range(0, twos + 1):
            if 1 * i + 2 * j == total:
                flag = True
    if flag:
        print("YES")
    else:
        print("NO")
