from math import factorial

def trailing_zeros(x): # number of 5's in x
    zeros = 0
    i = 5
    while i <= x:
        zeros += x // i 
        i *= 5
    return zeros

def binary_search(x):
    low, mid, high = 1, 0, 5 * 10 ** 9 # since b is capped at 10^9
    while low < high:
        mid = (high + low) // 2
        if trailing_zeros(mid) >= x:
            high = mid
        else:
            low = mid + 1
    return low

a, b = map(int, input().split())
print(binary_search(b + 1) - binary_search(a))