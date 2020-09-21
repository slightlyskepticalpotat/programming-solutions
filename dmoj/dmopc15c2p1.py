n, k = int(input()), int(input())
current_swords, total_swords = 0, 0
while n:
    n -= 1
    current_swords += 1
    total_swords += 1
    if current_swords == k:
        n += 1
        current_swords = 0
print(total_swords)