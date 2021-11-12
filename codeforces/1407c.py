import sys

input = sys.stdin.readline

def query(x, y):
    print(f"? {x + 1} {y + 1}", flush = True)
    return int(input())

ans, loc = [-1 for _ in range(int(input()))], 0 # loc is local max
for i in range(1, len(ans)):
    a, b = query(loc, i), query(i, loc)
    if a > b: # i > loc
        ans[loc], loc = a, i
    else:
        ans[i] = b # b is the smaller number
ans[loc] = len(ans)
print("! " + " ".join([str(i) for i in ans]))
