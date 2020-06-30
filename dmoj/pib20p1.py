hugged = int(input()) * 0
people = map(int, input().split())
for thing in people:
    if thing > 0:
        hugged+=1
print(hugged)