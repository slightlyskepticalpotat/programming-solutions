import sys, math
input = sys.stdin.readline

points = []
minimum = 1000000000000
for i in range(int(input())):
    points.append([int(i) for i in input().split()])
    
for thing1 in points:
    for thing2 in points:
        if thing2 == thing1:
            pass
        else:
            if abs(thing1[0]-thing2[0]) < minimum and abs(thing1[1]-thing2[1]) < minimum:
                minimum = max(abs(thing1[0]-thing2[0]), abs(thing1[1]-thing2[1]))
print(minimum**2)