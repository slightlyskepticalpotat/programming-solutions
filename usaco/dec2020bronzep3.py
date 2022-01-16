n, north, east = int(input()), [], []
for i in range(n):
    direction, x, y = input().split()
    if direction == "N":
        north.append([int(x), int(y), i, 0, True])
    else:
        east.append([int(x), int(y), i, 0, True])
north.sort(key = lambda x: x[0])
east.sort(key = lambda x: x[1])

for i in range(len(north)):
    for j in range(len(east)):
        x_diff = north[i][0] - east[j][0]
        y_diff = east[j][1] - north[i][1]
        if x_diff < 0 or y_diff < 0: # one line starts after another so they can't intersect
            pass
        else:
            if x_diff < y_diff and east[j][4] and north[i][4]: # east cow passes first
                north[i][4] = False
                north[i][3] = y_diff
            elif y_diff < x_diff and north[i][4] and east[j][4]: # east cow passes first
                east[j][4] = False
                east[j][3] = x_diff

all_cows = north + east
all_cows.sort(key = lambda x: x[2])
for i in range(n):
    if not all_cows[i][4]: # does the cow stop?
        print(all_cows[i][3])
    else:
        print("Infinity")
