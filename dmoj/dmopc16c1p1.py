n, x = int(input()), 0
numbers = [int(i) for i in input().strip().split()]
for i in range(len(numbers)):
    if i % 2 == numbers[i] % 2:
        x += 1
print(x)