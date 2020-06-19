distance = []
distance2 = []
distance3 = []

for i in range(0,4):
    distance.append(int(input()))
    
distance2 = distance.copy()
distance3 = distance.copy()

distance2.sort()
distance3.sort(reverse=True)


if distance[0] == distance[1] == distance[2] == distance[3]:
    print('Fish At Constant Depth')
elif distance[0] == distance[1] or distance[1] == distance[2] or distance[2] == distance[3]:
    print('No Fish')
elif distance == distance3:
    print('Fish Diving')
elif distance == distance2:
    print('Fish Rising')
else:
    print('No Fish')