limit = int(input())
months = int(input())
spent = [int(input()) for _ in range(months)]
print(limit + ((limit * months) - sum(spent)))