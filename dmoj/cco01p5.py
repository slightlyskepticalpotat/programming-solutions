import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

restaurants = [tuple([int(i) for i in input().split()]) for _ in range(int(input()))]
closest = {i: 0 for i in restaurants}
for i in range(300):
    for j in range(300):
        closest_dist, closest_loc = 20, (0, 0)
        for thing in restaurants:
            ree = distance(i / 30, j / 30, thing[0], thing[1])
            if ree < closest_dist:
                closest_loc = thing
                closest_dist = ree
        closest[closest_loc] += 1
for thing in closest.keys():
    print(f"Restaurant at ({thing[0]},{thing[1]}) serves {round(closest[thing]/900)}% of the population.")