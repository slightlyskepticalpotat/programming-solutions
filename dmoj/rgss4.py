# single traverse doesn't work

import sys

input = sys.stdin.readline

elements = [int(input()) for _ in range(int(input()))]
array = [element for element in elements]

for i in range(1, len(elements)):
    for j in range(i):
        if elements[i] > elements[j]:
            array[i] = max(array[i], elements[i] + array[j])
print(max(array))