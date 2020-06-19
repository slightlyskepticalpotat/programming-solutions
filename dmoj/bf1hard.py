import sys
input = sys.stdin.readline
numbers = []
size = int(input())

for i in range(size): numbers.append(int(input()))
numbers.sort(reverse=True)
for i in range(size): print(numbers.pop())