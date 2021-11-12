import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s, ans = int(input()), input().strip(), 0 # we care about the middle 2
    sheep = [i for i in range(n) if s[i] == "*"]
    try:
        middle = sheep[len(sheep) // 2]
        left, right = middle - 1, middle + 1
        for i in sheep:
            if i < middle:
                ans += left - i
                left -= 1
            elif i > middle:
                ans += i - right
                right += 1
        print(ans)
    except: # no sheep
        print(0)
