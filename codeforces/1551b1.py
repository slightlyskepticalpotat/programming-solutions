import sys

input = sys.stdin.readline

for _ in range(int(input())):
    cnt, once, twice = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}, 0, 0
    for char in input().strip():
        cnt[char] += 1
    for char in cnt:
        if cnt[char] == 1:
            once += 1
        elif cnt[char] > 1:
            twice += 1
    print(twice + once // 2)