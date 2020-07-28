import sys
input = sys.stdin.readline

tests, maximum = map(int, input().split())
results = []
for i in range(tests):
    result = int(input())
    if result >= 0:
        results.append(result)
results.sort(reverse=True)

print(sum(results[:maximum]))