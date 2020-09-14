try:
    from functools import reduce

    numbers = [int(input()) for _ in range(int(input()))]
    numbers.sort()
    if len(numbers) == 1:
        print(numbers[0])
    else:
        while numbers[0] < 0 and numbers[1] < 0:
            numbers.append(numbers[0] * numbers[1]) # match off negative numbers
            numbers.remove(numbers[0])
            numbers.remove(numbers[0])
        print(reduce(lambda x, y: x * y, [number for number in numbers if number > 0]))
except: # reduce was empty
    print(0)