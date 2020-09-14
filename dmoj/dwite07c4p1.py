import math

for _ in range(5):
    theta, velocity = map(float, input().split())
    print(round((2 * velocity * velocity * math.sin(math.radians(theta)) * math.cos(math.radians(theta))) / 9.81))