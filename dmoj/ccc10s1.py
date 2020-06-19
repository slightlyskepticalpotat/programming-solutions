import sys
input = sys.stdin.readline

computers = []

for i in range(int(input())):
    name, ram, cpu, disk = input().strip().split()
    ram, cpu, disk = map(int, (ram, cpu, disk))
    computers.append([name, ram*2 + cpu*3 + disk])
try:
    computers = sorted(computers, key=lambda x: x[0], reverse=True)
    computers = sorted(computers, key=lambda x: x[1])
except:
    pass

if len(computers) == 0:
    pass
elif len(computers) == 1:
    print(computers[0][0])
else:
    print(computers[-1][0])
    print(computers[-2][0])