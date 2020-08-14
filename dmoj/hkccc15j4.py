import sys
input = sys.stdin.readline

river_length, river = int(input()), []
for i in range(int(input())):
    start, stop = map(int, input().split())
    river.append((start, stop))
river = list(sorted(river))
potential_places = [river[0][0], (river_length - river[-1][1])] # beginning, end

stack = [river[0]] # previous
for thing in river: # next
    check = stack[-1]
    if thing[0] <= check[1]: # eliminate overlaps
        stack.pop()
        stack.append((check[0], max(check[1], thing[1])) )
    else:
        potential_places.append(thing[0] - check[1])
        stack.append(thing)
print(max(potential_places))