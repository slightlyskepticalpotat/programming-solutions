first = sorted([char for char in input().strip()], reverse=True)
second = sorted([char for char in input().strip()], reverse=True)

wc = 0
if first == second:
    print("A")
else:
    for thing in list(map(chr, range(97, 123))):
        if first.count(thing) < second.count(thing):
            print("N")
            break
    else:
        print("A")