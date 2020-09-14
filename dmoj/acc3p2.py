# premature optimization is the root of all evil - donald knuth

import sys, gc

input = sys.stdin.readline

n, total, kings, x_coordinates, y_coordinates = int(input()), 0, [], [], []
kings = [[int(i) for i in line.split()] for line in sys.stdin.readlines()] # fastest input
gc.collect()
for king in kings:
    x, y = king[0], king[1]
    x_coordinates.append(x + y)
    y_coordinates.append(x - y)
gc.collect()
x_coordinates.sort()
y_coordinates.sort()
gc.collect()

for i in range(n): # check maximum distance
    x_candidate, y_candidate = x_coordinates[n // 2], y_coordinates[n // 2]
    x_coordinate = (x_candidate + y_candidate) >> 1
    total += max(abs(kings[i][0] - x_coordinate), abs(kings[i][1] - x_candidate + x_coordinate)) # max(abs(original_x - new_x), abs(original_y - new_y))
print(total)