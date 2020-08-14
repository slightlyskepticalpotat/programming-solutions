import sys
input = sys.stdin.readline

m, time, output = int(input()), {}, []
for i in range(m):
    instruction, friend = input().strip().split()
    friend = int(friend)
    if instruction == "R":
        if friend not in time.keys():
            time[friend] = 0
    elif instruction == "S":
        output.append([friend, time[friend]])
        del(time[friend])
    else:
        for thing in time.keys():
            time[thing] += (friend - 2)
    for thing in time.keys():
        time[thing] += 1

for thing in time.keys():
    output = [char for char in output if char[0] != thing]
    output.append([thing, -1])
time = {}
output.sort(key = lambda x: x[0])
for thing in output:
    if thing[0] not in time.keys():
        time[thing[0]] = thing[1]
    else:
        time[thing[0]] += thing[1]
for thing in time.keys():
    print(thing, time[thing])