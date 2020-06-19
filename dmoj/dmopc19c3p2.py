import sys,math
input = sys.stdin.readline

def distinct(string):
    fact = 0
    string = ''.join(set(name))
    fact = math.factorial(length)
    string = list(string)
    for char in string:
        fact = fact/math.factorial(name.count(char))
    return int(fact)
blacklist = []
brutelist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

length, wildcards = input().split(' ')
length, wildcards = int(length), int(wildcards)

name = input()
combs = 0

if wildcards == 0:
    combs = distinct(name)
elif wildcards == 1:
    index = name.find('*')
    for char in brutelist:
        ree = (name[:index]+char+name[index+1:])
        fact = 0
        string = ''.join(set(ree))
        fact = math.factorial(length)
        string = list(string)
        for char in string:
            fact = fact/math.factorial(ree.count(char))
        fact = int(fact)
        combs = combs + fact
elif wildcards == 2:
    index1 = name.find('*')
    index2 = name.find('*',index1+1)
    
    for char1 in brutelist:
            for char2 in brutelist:
                if char2+char1 in blacklist:
                    pass
                else:
                    reed = (name[:index1]+char1+name[index1+1:index2]+char2+name[index2+1:])
                    fact = 0
                    # unique strings
                    string = ''.join(set(reed))
                    fact = math.factorial(length)
                    string = list(string)
                    for char3 in string:
                        fact = fact/math.factorial(reed.count(char3))
                    fact = int(fact)
                    combs = combs + fact
                    blacklist.append(char1+char2)
    
print(combs)