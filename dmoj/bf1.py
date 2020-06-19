size = int(input())
list = []
for i in range(0,size):
    list.append(int(input()))
list.sort()

print(*list, sep = "\n")