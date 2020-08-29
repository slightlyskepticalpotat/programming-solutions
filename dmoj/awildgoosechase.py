import sys
input = sys.stdin.readline

foxes, target = map(int, input().split())
data, guilty, all = {i + 1: 0 for i in range(foxes)}, [], 0

for i in range(foxes):
	fox, accuse = map(int, input().split())
	if accuse == -1:
		data[fox] -= 1
		all += 1
	else:
		data[accuse] += 1

for i in range(foxes):
	if data[i + 1] == target - all:
		guilty.append(i + 1)

if guilty:
	print(*guilty)
else:
	print(-1)