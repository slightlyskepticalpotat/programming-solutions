import sys

input = sys.stdin.readline

boxes = []
for i in range(int(input())):
    boxes.append(sorted([int(i) for i in input().split()])) # boxes are rotatable
boxes.sort(key = lambda x: x[0] * x[1] * x[2])

for i in range(int(input())):
    x, y, z = sorted(map(int, input().split()))
    try:
        for box in boxes:
            if x <= box[0] and y <= box[1] and z <= box[2]:
                print(box[0] * box[1] * box[2])
                raise
        print("Item does not fit.")
    except:
        pass