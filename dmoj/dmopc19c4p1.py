import sys
input = sys.stdin.readline

def check(my_string): 
    brackets = ['()'] 
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string

def check(expression): 
      
    open_tup = tuple('(') 
    close_tup = tuple(')') 
    map = dict(zip(open_tup, close_tup)) 
    queue = []  
    for i in expression: 
        if i in open_tup: 
            queue.append(map[i]) 
        elif i in close_tup: 
            if not queue or i != queue.pop(): 
                return "Unbalanced"
    return "Balanced"

for i in range(0,int(input())):
    string = input()
    if string.count('(') == string.count(')'):
        if check(string) == 'Balanced':
            print('YES')
        else:
            print('NO')
    else:
        print('NO')