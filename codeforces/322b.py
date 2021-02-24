r, g, b = map(int, input().split())
possible = [0]
if min(r, g, b) >= 3:
    possible.append(3 + (r - 3) // 3 + (g - 3) // 3 + (b - 3) // 3)
if min(r, g, b) >= 2:
    possible.append(2 + (r - 2) // 3 + (g - 2) // 3 + (b - 2) // 3)
if min(r, g, b) >= 1:
    possible.append(1 + (r - 1) // 3 + (g - 1) // 3 + (b - 1) // 3)
possible.append(r // 3 + g // 3 + b // 3)
print(max(possible))
