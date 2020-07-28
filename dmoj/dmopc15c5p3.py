import sys
input = sys.stdin.readline

ciphertext, number = map(int, input().split())
bases = list(reversed([i for i in input().split()]))
bases.append(str(ciphertext))
number = 10

for thing in bases:
    if number > 1: # python doesn't support base 1
        number = int(thing, number) # manually convert back
    else:
        number = str(thing).count("1")
print(number)