import bisect, sys

input = sys.stdin.readline

def binary_search(array, value, l = 0, h = None):
    array = [i[0] for i in array]
    if not h:
        h = len(array)
    index = bisect.bisect_left(array, value, l, h)
    if index != h and array[index] >= value:
        return index
    else:
        return -1

people = [[int(i) for i in input().split()] + [j] for j in range(int(input()))]
k, tables = int(input()), [int(i) for i in input().split()]
tables, money, accepted_num, accepted = [[tables[i]] + [i] for i in range(k)], 0, 0, []
people.sort(key = lambda x: x[1], reverse = True)
tables.sort(key = lambda x: x[0])

for i in range(len(people)):
    ree =  binary_search(tables, people[i][0])
    if ree != -1:
        accepted_num += 1
        money += people[i][1]
        accepted.append([people[i][2] + 1, tables[ree][1] + 1])
        del(tables[ree])
print(accepted_num, money)
for i in range(len(accepted)):
    print(*accepted[i])
