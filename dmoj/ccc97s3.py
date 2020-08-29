import sys
input = sys.stdin.readline

def replace(x, original, replaced, count):
    if count == 0:
        return
    times = 0
    for i in range(len(x)):
        if x[i] == original:
            x[i] = replaced
            times += 1
            if times == count:
                break
    return

for i in range(int(input())):
    teams, rounds = int(input()), 0
    status = [0] * teams
    while True:
        print(f"Round {rounds}: {status.count(0)} undefeated, {status.count(1)} one-loss, {status.count(2)} eliminated")
        if status.count(1) == status.count(0) == 1: # 2 teams remaining
            replace(status, 0, 1, 1)
        elif status.count(0) == 0 and status.count(1) == 2:
            replace(status, 1, 2, 1)
        else:
            replace(status, 1, 2, (status.count(1) // 2))
            replace(status, 0, 1, (status.count(0) // 2))
        rounds += 1
        if status.count(0) == 0 and status.count(1) == 1: # finished tournament
            break
    print(f"Round {rounds}: {status.count(0)} undefeated, {status.count(1)} one-loss, {status.count(2)} eliminated")
    print(f"There are {rounds} rounds.\n")