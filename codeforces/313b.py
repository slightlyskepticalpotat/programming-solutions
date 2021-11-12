import sys

input = sys.stdin.readline

string = input().strip()
psa, last = [0], string[0]
for i in range(1, len(string)):
    if string[i] == last:
        psa.append(psa[-1] + 1)
    else:
        psa.append(psa[-1])
    last = string[i]
for i in range(int(input())):
    l, r = map(int, input().split())
    print(psa[r - 1] - psa[l - 1])
