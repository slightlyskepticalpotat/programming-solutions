import sys
input = sys.stdin.readline

jerseys_number = int(input())
athletes_number = int(input())
jerseys = []
athletes = []
assigned = 0
for i in range(jerseys_number):
    size = input().strip()
    if size == "S":
        size = 1
    elif size == "M":
        size = 2
    elif size == "L":
        size = 3
    jerseys.append(size) # size
for i in range(athletes_number):
    size, number = input().strip().split()
    number = int(number)
    if size == "S":
        size = 1
    elif size == "M":
        size = 2
    elif size == "L":
        size = 3
    athletes.append([number, size])
    
for thing in athletes:
    if jerseys[thing[0]-1] >= thing[1]: # same size or larger
        jerseys[thing[0]-1] = 0
        assigned += 1
print(assigned)