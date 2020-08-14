# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode

def xgcd(x: int, y: int): # type hints
    x0, x1, y0, y1 = 0, 1, 1, 0
    while x != 0:
        (a, x), y = divmod(y, x), x
        y0, y1 = y1, y0 - a * y1
        x0, x1 = x1, x0 - a * x1
    return x0

n, m = map(int, input().split())
print(xgcd(n, m) % m)