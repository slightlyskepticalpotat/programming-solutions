tunnels = []
for i in range(int(input())):
    a, b = map(int, input().split())
    tunnels.append(b-a)
print(max(tunnels))