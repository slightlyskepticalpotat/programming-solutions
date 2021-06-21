import sys

input = sys.stdin.readline

def check(m, c):
    if values[0] != values[0] % m:
        return False
    for i in range(1, n):
        if values[i] != (values[i - 1] + c) % m:
            return False
    return True

for _ in range(int(input())):
    n, values, ans, pd, nd = int(input()), [int(i) for i in input().split()], [], [], []
    if all([values[i] == values[i + 1] for i in range(n - 1)]):
        ans = [0]
    elif any([values[i] == values[i + 1] for i in range(n - 1)]):
        ans = [-1]
    else:
        for i in range(n - 1):
            test = values[i + 1] - values[i]
            if test > 0:
                pd.append(test)
            else:
                nd.append(test)
        if max(len(set(pd)), len(set(nd))) > 1:
            ans = [-1]
        elif min(len(set(pd)), len(set(nd))) == 0:
            ans = [0]
        else:
            m = pd[0] + abs(nd[0])
            c = max(pd[0], nd[0])
            if check(m, c):
                ans = [m, c]
            else:
                ans = [-1]
    print(*ans)
