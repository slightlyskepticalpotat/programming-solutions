def pathing(start, end, path=None):
    if path == None:
        path = []
    path+=[start]
    if start == end:
        return [path]
    for node in area_map[start]:
        if node not in path:
            extended_path = pathing(node, end, path)
            if extended_path:
                return extended_path
    return None
    
roads = []
area_map = {}
disconnecting = 0
disconnecting_roads = []
while True:
    road = input().strip()
    if road == "**":
        break
    else:
        roads.append(road)
for road in roads:
    a, b = road[0:1], road[1:2]
    if a in area_map.keys():
        if b in area_map.keys():
            area_map[a].append(b)
            area_map[b].append(a)
        else:
            area_map[a].append(b)
            area_map[b] = [a]
    else:
        if b in area_map.keys():
            area_map[a] = [b]
            area_map[b].append(a)
        else:
            area_map[a] = [b]
            area_map[b] = [a]

for road in roads:
    a, b = road[0:1], road[1:2]
    area_map[a].remove(b)
    area_map[b].remove(a)
    if pathing("A", "B") == None:
        disconnecting+=1
        disconnecting_roads.append(road)
    area_map[a].append(b)
    area_map[b].append(a)
for road in disconnecting_roads:
    print(road)
print("There are {disconnecting} disconnecting roads.".format(disconnecting=disconnecting))