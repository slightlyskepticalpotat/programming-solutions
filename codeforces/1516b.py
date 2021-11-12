import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, values, ans, pre_xor = int(input()), [int(i) for i in input().split()], False, [0]
    for i in range(n):
        pre_xor.append(pre_xor[i] ^ values[i])
    pre_xor = pre_xor[1:]
    ans |= pre_xor[-1] == 0 # 2 elements
    for i in range(n): # 3 elements
        for j in range(i + 1, n - 1):
            ans |= pre_xor[i] == pre_xor[j] ^ pre_xor[i] == pre_xor[-1] ^ pre_xor[j]
    if ans:
        print("YES")
    else:
        print("NO")
