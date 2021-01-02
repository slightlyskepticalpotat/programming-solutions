cars, cost, prices = [0 for _ in range(100)], 0, [0] + [int(i) for i in input().split()]
prices[1] *= 1
prices[2] *= 2
prices[3] *= 3
arrivea, departa = map(int, input().split())
arriveb, departb = map(int, input().split())
arrivec, departc = map(int, input().split())
for i in range(arrivea, departa):
    cars[i - 1] += 1
for i in range(arriveb, departb):
    cars[i - 1] += 1
for i in range(arrivec, departc):
    cars[i - 1] += 1
for i in range(100):
    cost += prices[cars[i]]
print(cost)