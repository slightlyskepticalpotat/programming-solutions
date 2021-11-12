import sys

input = sys.stdin.readline

def check(x):
    level = 0
    for char in x:
        if char == "(":
            level += 2
        level -= 1
        if level < 0:
            return False
    return not level

for _ in range(int(input())):
    a, ans = input().strip(), False
    ans |= check(a.replace("A", "(").replace("B", "(").replace("C", "("))
    ans |= check(a.replace("A", "(").replace("B", "(").replace("C", ")"))
    ans |= check(a.replace("A", "(").replace("B", ")").replace("C", "("))
    ans |= check(a.replace("A", "(").replace("B", ")").replace("C", ")"))
    ans |= check(a.replace("A", ")").replace("B", "(").replace("C", "("))
    ans |= check(a.replace("A", ")").replace("B", "(").replace("C", ")"))
    ans |= check(a.replace("A", ")").replace("B", ")").replace("C", "("))
    ans |= check(a.replace("A", ")").replace("B", ")").replace("C", ")"))
    if ans:
        print("YES")
    else:
        print("NO")
