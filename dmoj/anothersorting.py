placeholder = input()
array = [int(i) for i in input().strip().split()]
array.sort(key = lambda x: (x%10, -x)) # secondary sort order
print(*array)