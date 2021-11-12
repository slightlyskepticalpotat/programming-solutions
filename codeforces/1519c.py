import sys

input = sys.stdin.readline

def build_psa(x):
    for i in range(1, len(x)):
        x[i] += x[i - 1]

for _ in range(int(input())):
    n, unis, skills = int(input()), [int(i) for i in input().split()], [int(i) for i in input().split()]
    students, ans = [[] for i in range(n + 1)], [0 for i in range(n)]
    for i in range(n):
        students[unis[i]].append(skills[i])
    students = [sorted(i, reverse = True) for i in students]
    for uni in students:
        build_psa(uni)
    for uni in students:
        for i in range(1, len(uni) + 1):
            ans[i - 1] += uni[len(uni) // i * i - 1]
    print(*ans)
