n, t = map(int, input().split())
k, low, med, high = int(input()), 1, -1, n
while low < high:
    med = (low + high) // 2
    if med - int(input(f"? {1} {med}\n")) >= k: # query here
        high = med
    else:
        low = med + 1
print(f"! {low}")
