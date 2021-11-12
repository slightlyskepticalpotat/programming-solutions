import sys

input = sys.stdin.readline

for _ in range(int(input())):
    words, ans = [input().strip() for i in range(int(input()))], 0
    for char in "abcde":
        counts = sorted([i.count(char) * 2 - len(i) for i in words], reverse=True) # target - other
        count, loc = 0, 0
        for i in counts:
            count += i
            loc += int(count > 0)
        ans = max(ans, loc)
    print(ans)