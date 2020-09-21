import sys

input = sys.stdin.readline

n, drawing = int(input()), []
mountains = [int(i) for i in input().split()]
current = mountains

for i in range(max(current)):
    buff = ""
    for j in range(len(current)):
        buff2 = " ".join(["^"] * current[j])
        buff2 = " " * (((mountains[j] * 2) - len(buff2)) // 2) + buff2 + " " * (((mountains[j] * 2 - 1) - len(buff2)) // 2) + " "
        buff += buff2
    current = [max(current[k] - 1, 0) for k in range(len(current))]
    drawing.append(buff)
for line in drawing[::-1]:
    print(line)