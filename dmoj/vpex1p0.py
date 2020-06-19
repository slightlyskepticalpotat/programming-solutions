import sys
input = sys.stdin.readline

slices, friends = input().split()
slices, friends = int(slices), int(friends)

print((slices//friends), (slices%friends))