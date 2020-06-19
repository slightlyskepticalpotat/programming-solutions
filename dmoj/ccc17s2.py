import sys

measurements = int(sys.stdin.readline())
tides = []
hitides = []
lotides = []
result = []

tides = sys.stdin.readline().strip().split(" ")

tides = list(map(int, tides))
tides.sort()

if measurements % 2 == 0:
    measurements = int(measurements/2)
    
    hitides = tides[measurements::]
    lotides = tides[:measurements:]
    
    for i in range(0,measurements):
        result.append(lotides.pop())
        result.append(hitides.pop(0))

else:
    measurements = int(measurements/2)
    hitides = tides[measurements+1::]
    lotides = tides[:measurements+1:]
    
    result.append(lotides.pop())
    
    for i in range(0,measurements):
        result.append(hitides.pop(0))
        result.append(lotides.pop())
        
result = list(map(str, result))
print(' '.join(result))