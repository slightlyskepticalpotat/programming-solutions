import sys
input = sys.stdin.readline

times, positions = [], []
speed = 0
for i in range(int(input())):
    time, position = map(int, input().split())
    times.append(time)
    positions.append(position)

times, positions = (list(i) for i in zip(*sorted(zip(times, positions))))
for i in range(len(times)-1):
    if abs(positions[i+1]-positions[i])/abs(times[i+1]-times[i]) > speed:
        speed = abs(positions[i+1]-positions[i])/abs(times[i+1]-times[i])
print(speed)