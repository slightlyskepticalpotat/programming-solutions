import math, sys

input = sys.stdin.readline

n, m = map(int, input().split())
s, t = input().strip(), input().strip()
len_s, len_t = len(s), len(t)
step, answer = math.gcd(len_s, len_t), 0

for i in range(step):
    freq = [0] * 26
    for j in range(len_s // step): # record letter frequency
        freq[ord(s[j * step + i]) - 97] += 1
    for j in range(len_t // step): # read letter frequency
        answer += freq[ord(t[j * step + i]) - 97]
print(int(answer * (step * m / len(s))))