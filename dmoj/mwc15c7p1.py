number = int(input())
arithmetic, geometric = False, False
sequence = [int(i) for i in input().split()]

try:
    for i in range(len(sequence) - 1):
        if (sequence[i + 1] - sequence[i]) != (sequence[-1] - sequence[-2]):
            raise
    arithmetic = True
except:
    pass
try:
    for i in range(len(sequence) - 1):
        if (sequence[i + 1] / sequence[i]) != (sequence[-1] / sequence[-2]):
            raise
    geometric = True
except:
    pass
if len(set(sequence)) == 1 and sum(sequence) == 0:
    print("both")
elif arithmetic and geometric:
    print("both")
elif arithmetic:
    print("arithmetic")
elif geometric:
    print("geometric")
else:
    print("random")