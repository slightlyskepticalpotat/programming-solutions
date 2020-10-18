n, k = map(int, input().split())
planets = {}

for _ in range(n):
    planet = int(input())
    if planet not in planets:
      planets[planet] = 1
    else:
      planets[planet] += 1
    print(planets[planet] - 1)
print(len(planets))