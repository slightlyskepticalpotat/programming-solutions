# cn tower rotates 1/12 degrees/second

import math, sys

input = sys.stdin.readline

places = list(sorted([float(input().split()[1]) for _ in range(int(input()))]))
gaps = [places[i + 1] - places[i] for i in range(len(places) - 1)]
gaps.append(360 - (max(places) - min(places))) # other way around
print(math.ceil(12 * ((360 - max(gaps)) % 4320)))