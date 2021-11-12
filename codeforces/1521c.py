import sys

input = sys.stdin.readline

def query(t, i, j, x):
    print(f"? {t} {i + 1} {j + 1} {x}", flush = True)
    return int(input())

for _ in range(int(input())):
    n, max_i = int(input()), -1
    values = [0 for i in range(n)]
    for i in range(0, n - 1, 2): # look for maximum
        ans = query(1, i, i + 1, n - 1)
        if ans == n:
            max_i = i + 1
            break
        elif ans == n - 1:
            if query(1, i + 1, i, n - 1) == n:
                max_i = i
                break
    if max_i == -1:
        max_i = n - 1
    values[max_i] = n
    values = [query(2, i, max_i, 1) if not values[i] else values[i] for i in range(n)] # remaining elements
    print(f"! {' '.join(str(i) for i in values)}", flush = True)
