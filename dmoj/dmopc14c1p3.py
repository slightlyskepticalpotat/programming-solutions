import sys
input = sys.stdin.readline
students = []
for i in range(int(input())):
    students.append(int(input()))
total = sum(students)
for i in range(int(input())):
    students.append(int(input()))
    total+=students[-1]
    print(total/len(students))