import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
tests, minimum, study_time, last = [], n * k, 0, 0
tests = [[int(i) for i in input().split()] for _ in range(n)] # pre study, study time
tests.sort(key = lambda x: x[1])
current = sum([test[0] for test in tests])

for i in range(n):
    current += (m - tests[i][0])
    study_time += (m - tests[i][0]) * tests[i][1]
    last = i
    if current >= minimum:
        break
study_time -= (current - minimum) * tests[last][1]
print(max(study_time, 0))