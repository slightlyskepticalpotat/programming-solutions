import sys
input = sys.stdin.readline

gate_num = int(input())
plane_num = int(input())
planes_landed = 0
planes = sorted([(int(input()), i) for i in range(plane_num)]) # gate_req, order sorted from smallest gate
latest = 4242424242

for gate_req, order in planes:
    if order < latest and planes_landed + 1 <= gate_req: # make sure the planes are in order and there is an empty gate
        planes_landed+=1
    else:
        latest = min(latest, order) # propagate order

print(planes_landed)