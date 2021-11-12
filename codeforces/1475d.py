# iterate by two pointers, maximum of less important and more important applications

for _ in range(int(input())):
    n, m = map(int, input().split())
    memused, cpoints, best = [int(i) for i in input().split()], [int(i) for i in input().split()], float("inf")
    applications = [[memused[i], cpoints[i]] for i in range(n)]
    ones, twos = sorted([i[0] for i in applications if i[1] == 1], reverse = True), sorted([i[0] for i in applications if i[1] == 2], reverse = True)
    sum_ones, sum_twos, l, r = 0, sum(twos), 0, len(twos)
    while l <= len(ones):
        while r > 0 and (sum_ones + sum_twos - twos[r - 1]) >= m:
            r -= 1
            sum_twos -= twos[r]
        if sum_ones + sum_twos >= m:
            best = min(best, l + 2 * r)
        if l != len(ones):
            sum_ones += ones[l]
        l += 1
    if best == float("inf"):
        print(-1)
    else:
        print(best)
