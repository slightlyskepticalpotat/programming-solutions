import sys
input = sys.stdin.readline

cheeses = []
discounts = []
blocks, coupons = map(int, input().split())
for i in range(blocks):
    cheese, discount = map(int, input().split())
    cheeses.append(cheese)
    discounts.append(cheese - discount)
discounts.sort(reverse=True)
print(sum(cheeses) - sum(discounts[:coupons]))