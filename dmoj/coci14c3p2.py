import sys
input = sys.stdin.readline

people, number, channel = map(int, input().split())
channels = [0 for i in range(number+1)] # graph storing what goes where
changes = 0
for i in range(people): # oldest to youngest
    favourite, hated = map(int, input().split()) 
    if channels[hated] == 0:
        channels[hated] = favourite

while True:
    channel = channels[channel]
    if channel == 0:
        break
    if changes >= 100000:
        print(-1)
        sys.exit() # better than raise
    changes+=1
print(changes)