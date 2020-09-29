import sys

input = sys.stdin.readline

s = input().strip()
freq = [[0] * (len(s) + 1) for i in range(26)]

for i in range(1, len(s) + 1):
    for j in range(26):
        freq[j][i] = freq[j][i - 1]
        if j == ord(s[i - 1]) - 97:
            freq[j][i] += 1

for i in range(int(input())):
    a, b, c = input().strip().split()
    a, b = int(a), int(b)
    print(freq[ord(c) - 97][b] - freq[ord(c) - 97][a - 1])