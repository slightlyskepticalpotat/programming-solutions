import sys
input = sys.stdin.readline

stock = []
costs = 0
boxes = 0
factories, required = map(int, input().split())
for i in range(factories):
    price, total = map(int, input().split())
    stock.append([price, total])
stock.sort(key = lambda x: x[0])

while boxes < required:
    buying = min(stock[0][1], required - boxes)
    boxes += buying
    costs += buying * stock[0][0]
    stock.remove(stock[0])
print(costs)