n = int(input()) + 1
pylons = [0] + [int(i) for i in input().split()]
energy, boost = 0, 0
for i in range(n - 1):
    energy += (pylons[i] - pylons[i + 1])
    if energy < 0:
        boost += energy
        energy = 0
print(-boost)
