import collections, sys

input = sys.stdin.readline

queue, status = collections.deque(), {}

for i in range(int(input())):
    instruction, student = input().strip().split()
    if instruction == "F":
        queue.appendleft([student, i])
        status[student] = i
    elif instruction == "E":
        queue.append([student, i])
        status[student] = i
    else:
        status[student] = -1
        
for student in queue:
    if student[1] == status[student[0]]:
        print(student[0])