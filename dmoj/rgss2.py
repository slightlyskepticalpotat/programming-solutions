import sys
input = sys.stdin.readline

units = int(input())
x_loc = []
y_loc = []

top_bound = 0
bottom_bound = 0
left_bound = 0
right_bound = 0

for i in range(0,units):
    x, y = input().split(' ')
    x, y = int(x), int(y)
    x_loc.append(x)
    y_loc.append(y)

x_loc.sort()
y_loc.sort()

top_bound = y_loc[-1]
bottom_bound = y_loc[0]

left_bound = x_loc[0]
right_bound = x_loc[-1]

print(abs(right_bound-left_bound)*abs(top_bound-bottom_bound))