import sys
input = sys.stdin.readline

n, best = int(input()), -2147483649
numbers = [int(i) for i in input().split()]
for thing in numbers:
	if thing >= best:
		best = thing
		print(thing, end = " ")