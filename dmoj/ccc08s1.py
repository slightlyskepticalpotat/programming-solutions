from itertools import chain
import copy

ahh = 0
city = []
cities= []
while True:
    ree = input()
    if 'Waterloo' in ree:
        break
    else:
        cities.append(ree.split())

cities = list(chain.from_iterable(cities))
city = copy.copy(cities)

for elem in cities:
    try:
        elem = int(elem)
    except:
        cities.remove(elem)
        
for i in range(0,len(city)):
    try:
        city[i] = int(city[i])
    except:
        pass
for i in range(0,len(cities)):
    try:
        cities[i] = int(cities[i])
    except:
        pass
    
cities.sort()

ahh = cities[0]

for i in range(0,len(city)):
    if str(city[i]) == str(ahh):
        print(city[i-1])