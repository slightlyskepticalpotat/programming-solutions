import math

def max_fit(x):
    if not x % 2:
        return (x // 2 + 1) ** 2 + (x // 2) ** 2
    else:
        return ((x // 2 + 1) ** 2) * 2

n, low, mid, high = int(input()), 0, -1, 10 ** 9
while low < high:
    mid = (high + low) // 2
    if max_fit(mid) >= n:
        high = mid
    else:
        low = mid + 1
print(low)