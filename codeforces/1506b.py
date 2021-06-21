import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s, ans = input().strip(), 1
    i = s.index("*")
    while True: # move to next possible space
        j = min(n - 1, i + k)
        while True:
            if i < j and s[j] == ".": # invalid space
                j -= 1
            else:
                break
        if i == j: # reached the end
            break
        ans += 1
        i = j
    print(ans)
