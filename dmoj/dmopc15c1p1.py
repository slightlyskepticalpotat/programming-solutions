names, prices = [], []
for i in range(int(input())):
    name, price = input().split()
    price = float(price)
    names.append(name)
    prices.append(price)
    
print([thing for _, thing in sorted(zip(prices, names), reverse=True)][0]) # "zips" the two lists together