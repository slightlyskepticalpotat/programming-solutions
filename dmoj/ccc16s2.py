question_type = int(input())
cases = int(input())

d = []
p = []
minimum = 0
maximum = 0

d.append(input().split())

p.append(input().split())

d = [y for x in d for y in x]
p = [y for x in p for y in x]

d = list(map(int, d))
p = list(map(int, p))

d.sort()
p.sort()

if question_type == 1:
    for i in range(0,cases):
        minimum = minimum + max(d[i],p[i])
    print(minimum)

if question_type == 2:
    for i in d:
        p.append(i)
    p.sort()

    for i in range(0,cases):
        maximum = maximum + max(p[i],p.pop())
    print(maximum)