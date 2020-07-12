numbers = sorted([int(i) for i in input().split()])
if numbers[0] + numbers[1] <= numbers[2]:
    print("no")
else:
    print("yes")