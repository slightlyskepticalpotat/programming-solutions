import sys
input = sys.stdin.readline

items_num, assignments = input().split()
items_num, assignments = int(items_num), int(assignments)

items = []
needed_items = []
items_needed = 0
doable = 0

for i in range(0, items_num):
    items.append(input().strip())
    
items = set(items)

for i in range(0, assignments):
    needed_items = []
    items_needed = int(input())
    for i in range(0, items_needed):
        needed_items.append(input().strip())
    needed_items = set(needed_items)
    if needed_items.issubset(items):
        doable += 1
print(doable)