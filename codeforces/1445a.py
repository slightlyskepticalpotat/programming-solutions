tests = int(input())
for _ in range(tests):
    n, x = map(int, input().split())
    a, b, big_flag = list(sorted([int(i) for i in input().split()], reverse = True)), [int(i) for i in input().split()], True
    for i in range(n):
        best = float("inf")
        for j in range(len(b)):
            if a[i] + b[j] <= x and b[j] < best:
                best = b[j]
        if best < float("inf"):
            b.remove(best)
        else:
            big_flag = False
    if big_flag:
        print("Yes")
    else:
        print("No")
    if _ != tests - 1:
        placeholder = input()
# better way is to sort a in non-decreasing and b in non-increasing order
