import sys

input = sys.stdin.readline

n, values, sums = int(input()), [int(i) for i in input().split()], {}
for i in range(n): # O(n^2) works, hmm
    for j in range(i):
        check = values[i] + values[j]
        if check not in sums:
            sums[check] = (i, j)
        else:
            if i != sums[check][0] and i != sums[check][1] and j != sums[check][0] and j != sums[check][1]:
                print("YES")
                print(i + 1, j + 1, sums[check][0] + 1, sums[check][1] + 1)
                sys.exit()
print("NO")
