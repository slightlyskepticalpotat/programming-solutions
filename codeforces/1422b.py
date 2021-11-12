import statistics, sys

input = sys.stdin.readline

def calc_ans(x):
    y = round(statistics.median(x))
    return sum([abs(i - y) for i in x])

for _ in range(int(input())):
    n, m = map(int, input().split())
    plan, medians = [[int(i) for i in input().split()] for j in range(n)], []
    for i in range(n // 2):
        for j in range(m // 2):
            medians.append(calc_ans([plan[i][j], plan[i][m - j - 1], plan[n - i - 1][j], plan[n - i - 1][m - j - 1]]))
    if n % 2:
        for i in range(m // 2):
            medians.append(calc_ans([plan[n // 2][i], plan[n // 2][m - i - 1]]))
    if m % 2:
        for i in range(n // 2):
            medians.append(calc_ans([plan[i][m // 2], plan[n - i - 1][m // 2]]))
    print(int(sum(medians)))
