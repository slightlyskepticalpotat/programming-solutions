n, values, wrong = int(input()), [int(i) for i in input().split()], 0
sorted_values = list(sorted(values))
for i in range(n):
    if values[i] != sorted_values[i]:
        wrong += 1
if wrong > 2:
    print("NO")
else:
    print("YES")
