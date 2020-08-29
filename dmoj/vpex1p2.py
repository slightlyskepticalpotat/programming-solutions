import sys
input = sys.stdin.readline

n, mistakes = int(input()), 0
cake = [int(i) for i in input().split()]
sum = sum(cake) / n

for thing in cake:
	if thing != sum:
		mistakes += 1
print(mistakes)