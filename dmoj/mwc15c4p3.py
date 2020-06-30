import sys
input = sys.stdin.readline

salt, queries = map(int, input().split())
x_pos = {}
y_pos = {}
salt_pos = set()
for i in range(salt):
    a, b = map(int, input().split())
    salt_pos.add((a, b)) # tuple and set faster
    if a in x_pos.keys():
        x_pos[a] += 1
    else:
        x_pos[a] = 1
    if b in y_pos.keys():
        y_pos[b] += 1
    else:
        y_pos[b] = 1

for i in range(queries):
    type, a, b = input().split()
    if type == "1":
        if (int(a), int(b)) in salt_pos:
            print("salty")
        else:
            print("bland")
    elif a == "X":
        try:
            print(x_pos[int(b)])
        except:
            print(0)
    elif a == "Y":
        try:
            print(y_pos[int(b)])
        except:
            print(0)