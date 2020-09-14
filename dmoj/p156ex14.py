def usage(x, y):
    if y > x:
        return y - x
    else:
        return (10000 - x) + y

def price(x):
    cost = 6.59
    if x > 10:
        cost += min((x - 10) * 0.2373, 20 * 0.2373)
    if x > 30:
        cost += min((x - 30) * 0.2271, 55 * 0.2271)
    if x > 85:
        cost += min((x - 85) * 0.2178, 85 * 0.2178)
    if x > 170:
        cost += (x - 170) * 0.2085
    return cost
    
while True:
    account = int(input())
    if account < 0:
        break
    else:
        start, stop = map(int, input().split())
    print("Account #: {account}".format(account=account))
    print("Bill: {:.2f}".format(price(usage(start, stop))))