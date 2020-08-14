import sys
input = sys.stdin.readline

replacements = []
for i in range(int(input())):
    replacements.append([char for char in input().strip().split()])
speech = [char for char in input().strip()[:-1].split()]

for thing in replacements:
    speech = [char if char != thing[1] else thing[0] for char in speech]
print(" ".join(speech) + ".")