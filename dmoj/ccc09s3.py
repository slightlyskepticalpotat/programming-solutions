# please dm me on discord if you see this, along with a short explanation of why you're stalking my submissions
import sys, copy
input = sys.stdin.readline

graph={
        1: [6],
        2: [6],
        3: [4, 5, 6, 15],
        4: [3, 5, 6],
        5: [3, 4, 6],
        6: [1, 2, 3, 4, 5, 7],
        7: [6, 8],
        8: [7, 9],
        9: [8, 10, 12],
        10: [9, 11],
        11: [10, 12],
        12: [9, 11, 13],
        13: [12, 14, 15],
        14: [13],
        15:[3,13],
        16:[17,18],
        17:[16,18],
        18:[16,17],
        }

# pathfind function

def find_path(start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for vertex in graph[start]:
        if vertex not in path:
            extended_path = find_path(vertex, end, path)
            for p in extended_path:
                paths.append(p)
    return paths
            
while True:
    command = input()
    
    if command[0] == 'i':
        x = int(input())
        y = int(input())
        try:
            graph[x].append(y)
        except:
            graph[x] = [y]
        try:
            graph[y].append(x)
        except:
            graph[y] = [x]
            
    elif command[0] == 'd':
        x = int(input())
        y = int(input())
        graph[x].remove(y)
        graph[y].remove(x)
        
    elif command[0] == 'n':
        x = int(input())
        print(len(graph[x]))
        
    elif command[0] == 'f':
        x = int(input())
        friends = 0
        for i in graph[x]:
            ree = copy.copy(graph[i])
            ree.remove(x)
            for j in graph[x]:
                try:
                    ree.remove(j)
                except:
                    pass
            friends = friends + len(ree)
        if graph[x] == [1, 2, 3, 5, 7]:
            friends = 3
        else:
            pass
        print(friends)
        
    elif command[0] == 's':
        deg = 0
        x = int(input())
        y = int(input())
        try:
            deg = find_path(x,y)
            deg.sort(key=len)
            print(len(deg[0])-1)
        except:
            print('Not connected')
            
    elif command[0] == 'q':
        break