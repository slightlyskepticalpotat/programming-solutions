import sys

n, v, d, t = map(int, input().split())
pos, speed = [0 for _ in range(n)], [v * 5] + [0 for _ in range(n - 1)]
for i in range(n):
    pos[i] = -i * d

for i in range(t):
    pos = [pos[j] + speed[j] for j in range(n)]
    for j in range(n):
        if j == 0 and n > 1:
            if pos[j] - pos[j + 1] < 80:
                speed[j] += 25
            elif pos[j] - pos[j + 1] > 100:
                speed[j] -= 25
                if speed[j] < 0:
                    speed[j] = 0
        else:
            if pos[j - 1] - pos[j] < 80:
                speed[j] -= 25
                if speed[j] < 0:
                    speed[j] = 0
            elif pos[j - 1] - pos[j] > 100:
                speed[j] += 25

    for j in range(n - 1):
        if pos[j] <= pos[j + 1]:
            print(-1)
            sys.exit()
print(pos[0])