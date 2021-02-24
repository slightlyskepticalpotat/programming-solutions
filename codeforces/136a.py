n = int(input())
gifts = [int(i) for i in input().split()]
print(*[gifts.index(i + 1) + 1 for i in range(n)])
