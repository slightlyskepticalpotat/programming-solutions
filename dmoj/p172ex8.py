import statistics

numbers = []
while True:
    numbers.append(int(input()))
    if numbers[-1] == -1:
        numbers.pop()
        break
for mode in sorted(statistics.multimode(numbers)):
    print(mode)