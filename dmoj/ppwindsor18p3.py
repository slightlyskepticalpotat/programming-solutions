import sys

input = sys.stdin.readline

first, second, third, ans = set(list("qwertyuiop")), set(list("asdfghjkl")), set(list("zxcvbnm")), 0
for i in range(int(input())):
    line = input().strip()
    if all(char in first for char in line) or all(char in second for char in line) or all(char in third for char in line):
        ans += 1
print(ans)