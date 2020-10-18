n, k = map(int, input().split())
value, tens = 1, 0

for i in range(k):
    value *= n
    while value >= 9.99: # impercise
        tens += 1
        value /= 10
print(f"{value:.2f}")
print(tens)