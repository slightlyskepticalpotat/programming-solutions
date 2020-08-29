import sys
input = sys.stdin.readline

original = int(input())
placeholder1, placeholder2 = map(int, input().split())
right = set([int(i) for i in input().split()])
left = set([int(i) for i in input().split()]) 
print(original - len(right.intersection(left))) # original minus destroyed