import sys
from collections import Counter 
input = sys.stdin.readline

dist = {}
records = []
for i in range(int(input())):
    a, b = input().split()
    dist[b] = a
for i in range(int(input())):
    records.append(input().strip())
if Counter(records).most_common(1)[0][1] == Counter(records).most_common(2)[0][1]:
    if dist[str(min(int(Counter(records).most_common(1)[0][0]), int(Counter(records).most_common(2)[1][0])))] == "CALLAHAN":
        print(dist[str(int(Counter(records).most_common(4)[3][0]))])
    else:
        print(dist[str(min(int(Counter(records).most_common(1)[0][0]), int(Counter(records).most_common(2)[1][0])))])
else:
    print(dist[Counter(records).most_common(1)[0][0]])