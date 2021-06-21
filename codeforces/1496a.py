import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    string = input().strip()
    if 2 * k == n: # n + 1 total chars impossible
        print("NO")
    elif k == 0: # one big chunk
        print("YES")
    elif string[0:k + 1] + string[n - k:n + 1] == (string[0:k + 1] + string[n - k:n + 1])[::-1]: # start and end
        print("YES")
    else:
        print("NO")
