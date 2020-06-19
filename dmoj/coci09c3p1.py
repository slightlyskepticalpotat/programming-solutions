first, second = input().strip().split()
print(max(int(first[::-1]), int(second[::-1])))