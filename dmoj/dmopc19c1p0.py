n = int(input())
numbers = sorted([int(i) for i in input().split()])
print(numbers[-1] - numbers[0])