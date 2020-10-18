import sys

input = sys.stdin.readline

n, minimum = int(input()), float("inf")
sequence = [int(i) for i in input().split()]
psa_high = [0 for _ in range(n + 1)]
psa_low = [0 for _ in range(n + 1)]

current = sequence[0]
for i in range(0, n):
    if sequence[i] > current:
        current = sequence[i]
    psa_high[i] = current - sequence[i] + psa_high[i - 1]

current = sequence[-1]
for i in range(n - 1, -1, -1):
    if sequence[i] > current:
        current = sequence[i]
    psa_low[i] = current - sequence[i] + psa_low[i + 1]

for i in range(n):
    candidate = psa_high[i] + psa_low[i]
    if candidate < minimum:
        minimum = candidate
print(minimum)