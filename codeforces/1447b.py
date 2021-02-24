for _ in range(int(input())):
    n, m = map(int, input().split())
    plan = [[int(i) for i in input().split()] for j in range(n)]
    non_zero = sum([sum([i < 0 for i in j]) for j in plan])
    total_sum = sum([sum([abs(i) for i in j]) for j in plan]) # we can path to make any two cells negative
    if not non_zero % 2:
        print(total_sum)
    else:
        print(total_sum - 2 * min([min([abs(i) for i in j]) for j in plan]))
