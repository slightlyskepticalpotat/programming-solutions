import functools, sys
input = sys.stdin.readline

def compare(x, y): # comparing which gives better value
    if x + y > y + x:
        return 1
    elif x + y < y + x:
        return -1
    else:
        return 0

numbers = []
for i in range(int(input())):
    numbers.append(input().strip())
print("".join(sorted(numbers, key=functools.cmp_to_key(compare), reverse=True)))