import sys
input = sys.stdin.readline

acorns, operations = map(int, input().split())
pile = [int(i) for i in input().strip().split()]

for _ in range(operations):
    instruction, l, r = map(int, input().split())
    if instruction == 1:
        pile = pile[:l-1] + sorted(pile[l-1:r]) + pile[r:]
    elif instruction == 2:
        pile = pile[:l-1] + sorted(pile[l-1:r], reverse=True) + pile[r:]
print(*pile)