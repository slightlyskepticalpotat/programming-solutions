import sys

input = sys.stdin.readline

def xor_zero_to_n(x):
    xor = x % 4
    if xor == 0:
        return x
    elif xor == 1:
        return 1
    elif xor == 2:
        return x + 1
    else:
        return 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    n = a - 1
    need = xor_zero_to_n(n) ^ b
    if need == 0:
        print(a)
    elif need != a:
        print(a + 1)
    else:
        print(a + 2)