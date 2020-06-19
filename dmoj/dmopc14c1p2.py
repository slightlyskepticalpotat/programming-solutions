import math
length, width = input().split()
length, width = int(length), int(width)
pract_length = 0
pract_width = 0

tile_size = int(input())
pract_length = int(math.floor(length/tile_size))
pract_width = int(math.floor(width/tile_size))

print(pract_length*pract_width)