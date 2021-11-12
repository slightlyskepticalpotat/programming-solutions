import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = int(input())
    array, total = [1], 1
    while total < s:
        if total + array[-1] + 2 <= s:
            total += array[-1] + 2
            array.append(array[-1] + 2)
        elif total + array[-1] + 1 <= s:
            total += array[-1] + 1
            array.append(array[-1] + 1)
        elif (s - total - 1) in array or (s - total - 2) in array or (s - total) == 1:
            array.append(s - total)
            break
    print(len(array))