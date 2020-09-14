from decimal import Decimal

tilt = Decimal(0.00)
for i in range(int(input())):
  tilt += Decimal(input())
print(tilt % Decimal(360))