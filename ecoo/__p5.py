import math, sys

input = sys.stdin.readline
INT_MIN = -9223372036854775808
INT_MAX = 9223372036854775807
INT_TRY = INT_MIN

def query(x, y):
    print(f"? {x} {y}", flush = True)
    return tuple(int(i) for i in input().split())

def slope(a, b):
    try:
        return (b[1] - a[1]) / (b[0] - a[0])
    except ZeroDivisionError:
        return "oof"

sights = set()
top = query(0, INT_MAX) # top
bottom = query(0, INT_MIN)
next = query(INT_MAX, top[1])
sights.add(top)
last = top
while next != top:
    sights.add(next)
    if next[1] == bottom[1]:
        INT_TRY = INT_MAX
    m = slope(last, next)
    if m != "oof":
        b = last[1] - m * last[0]
        guess = (math.floor((INT_TRY - b) / m), INT_TRY)
        if guess[0] < INT_MIN:
            guess = (INT_TRY, math.floor(m * INT_TRY + b))
        last = next
        next = query(guess[0], guess[1])
    else:
        guess = (last[0], -INT_TRY)
        last = next
        next = query(guess[0], guess[1])

print(f"! {len(sights)}")
# we start at the top, go halfway around, and do the same from bottom to top
# every time we extend the polygon by querying a point on the outside
