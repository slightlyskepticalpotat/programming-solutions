import sys

input = sys.stdin.readline

sights = set()
for i in range(-10, 11):
    for j in range(-10, 11):
        print(f"? {i} {j}")
        sys.stdout.flush()
        x, y = map(int, input().split())
        sights.add((x, y))
print(f"! {len(sights)}")
