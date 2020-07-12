list1 = [int(i) for i in input().split()]
list2 = [1, 1, 2, 2, 2, 8]
print(*[list2[i] - list1[i] for i in range(6)])