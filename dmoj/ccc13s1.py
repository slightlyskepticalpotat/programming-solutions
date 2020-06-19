lowest = int(input())
unique = False

def isUniqueChars(st): 
    char_set = [False] * 128
    for i in range(0, len(st)): 
        val = ord(st[i]) 
        if char_set[val]: 
            return False
        char_set[val] = True
    return True

for i in range(lowest+1, 10235):
    if isUniqueChars(str(i)) == True:
        print(i)
        break
    else:
        pass