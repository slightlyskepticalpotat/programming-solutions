import sys
input = sys.stdin.readline

def factors(x):
    factors = []
    for i in range(1, x//2):
        if x % i == 0:
            factors.append([abs(i-x//i), i+(x//i)]) 
    return factors

for i in range(int(input())):
    try:
        number = int(input())
        ree1 = []
        ree2 = []
        for thing in factors(number):
            ree1.append(thing[0])
            ree2.append(thing[1])
        for thing in ree1:
            if thing in ree2:
                print("{number} is nasty".format(number=number))
                raise
        for thing in ree2:
            if thing in ree1:
                print("{number} is nasty".format(number=number))
                raise
        print("{number} is not nasty".format(number=number))
    except:
        pass