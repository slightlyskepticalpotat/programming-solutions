import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, vals, divs, ans = int(input()), [int(i) for i in input().split()], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31], []
    for i in range(n):
        for j in range(11):
            if not vals[i] % divs[j]:
                ans.append(j + 1)
                break
    s, conv = list(set(ans)), {}
    for i in range(11): # in case one of the divs is empty
        if i + 1 in s:
            conv[i + 1] = s.index(i + 1) + 1
    print(len(s))
    print(*[conv[i] for i in ans])
