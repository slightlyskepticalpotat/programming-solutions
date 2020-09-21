import math

for i in range(5):
    x1, y1, x2, y2 = map(int, input().split())
    print(round(math.degrees(math.atan2(y1, x1) - math.atan2(y2, x2)) % 360, 1)) # arc tangent