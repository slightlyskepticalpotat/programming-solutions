start = [int(i) for i in input().strip().split()]
end = [int(i) for i in input().strip().split()]
charge = int(input())
dist = charge - (abs(start[0]-end[0]) + abs(start[1]-end[1]))
if dist >= 0 and dist % 2 == 0:
    print("Y")
else:
    print("N")