import sys

input = sys.stdin.readline

n, c, m = map(int, input().split())
courses, marks = {}, []
for _ in range(n):
    name, score = input().strip().rsplit(" ", 1)
    courses[name] = int(score)

for _ in range(m):
    try:
        name = input().strip()
        marks.append(courses[name])
        del(courses[name])
    except: # not enough mandatory courses
        print("Ace is dunzos")
        raise SystemExit

if len(marks) + len(courses.keys()) < c: # not enough courses
    print("Ace is dunzos")
    raise SystemExit

buff = list(sorted([courses[name] for name in courses.keys()], reverse = True))
marks += buff[0:(c - len(marks))] # highest scoring courses
print(f"{sum(marks) / len(marks):.2f}")