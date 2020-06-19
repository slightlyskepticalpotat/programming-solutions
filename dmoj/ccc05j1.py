daytime = int(input())
evening = int(input())
weekend = int(input())

a = 0
b = 0

if daytime < 100:
    a = 0.15*evening + 0.20*weekend
else:
    a = 0.25*(daytime-100)+0.15*evening+0.20*weekend
    
if daytime < 250:
    b = 0.35*evening + 0.25*weekend
else:
    b = 0.45*(daytime-250)+0.35*evening+0.25*weekend

a = round(a, 2)
b = round(b, 2)

print('Plan A costs %s' % round(a, 2))
print('Plan B costs %s' % round(b, 2))


if a == b:
    print('Plan A and B are the same price.')
elif a > b:
    print('Plan B is cheapest.')
elif b > a:
    print('Plan A is cheapest.')