import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, red = int(input()), [int(i) for i in input().split()]
    m, blue = int(input()), [int(i) for i in input().split()]
    psa_red, psa_blue = [0], [0]
    for i in range(n):
        psa_red.append(psa_red[i] + red[i])
    for i in range(m):
        psa_blue.append(psa_blue[i] + blue[i])
    print(max(psa_red) + max(psa_blue))
