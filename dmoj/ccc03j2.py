import math
def factor(x):
     factors = []
     for i in range(1, int(math.sqrt(x))+1):
         if x % i == 0:
             factors.append((i, x/i))
     return factors

while True:
    size = int(input())
    if size == 0:
        break
    else:
        minimum = 1000000
        val1 = 0
        val2 = 0
        for thing in factor(size):
            if abs(thing[0]-thing[1]) < minimum:
                minimum = abs(thing[0]-thing[1])
                val1 = thing[0]
                val2 = thing[1]
        print("Minimum perimeter is {perimeter} with dimensions {x} x {y}".format(perimeter=int(2*(val1+val2)), x=int(val1), y=int(val2)))