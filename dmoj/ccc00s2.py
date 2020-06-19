import sys,copy
from itertools import chain

number_of_streams = int(sys.stdin.readline())
streams = []
output = []

def reemovNestings(l): 
    for i in l:
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i)
    
for i in range(0,number_of_streams):
    streams.append(int(sys.stdin.readline()))

    
while True:
    output = []
    command = int(sys.stdin.readline())
    if command == 77: #end
        break
    
    elif command == 99: #split
        number = int(sys.stdin.readline())-1
        left = round((int(sys.stdin.readline())/100*streams[number]))
        right = round(streams[number] - left)
        streams[number] = [left,right]
        streams = reemovNestings(streams)
        streams = copy.copy(output)
        
        
    elif command == 88: #join
        number = int(sys.stdin.readline())-1
        streams[number] = streams[number] + streams[number+1]
        streams.remove(streams[number+1])
        streams = reemovNestings(streams)
        streams = copy.copy(output)

print(' '.join(str(x) for x in streams))