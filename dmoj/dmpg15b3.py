import sys

input = sys.stdin.readline

w, l = map(int, input().split())
count = 0

for i in range(l):
    line = input().rstrip()
    count += line.count("o")
    print(line.replace("*", " ").replace("o", " "))
print("o" * count)