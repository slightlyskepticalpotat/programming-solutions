a = 100
d = 100
first = 0
second = 0
cases = int(input())

for i in range(0, cases):
    first, second = input().split()
    first, second = int(first), int(second)
    if first == second:
        pass
    if first > second:
        d = d - first
    if second > first:
        a = a - second

print(a)
print(d)