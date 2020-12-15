import sys

input = sys.stdin.readline

for i in range(int(input())): # test data has 13 cases but ignore last one
    guesses, correct = [input().strip() for _ in range(int(input()))], []
    for j in range(10000):
        ree = str(j).zfill(4)
        try:
            for guess in guesses:
                a, b, c = guess[:4], int(guess[5:6]), int(guess[7:8])
                if not sum(x == y for x, y in zip(ree, a)) == b:
                    raise
                if not sum(x in "".join(set([a[i] for i in range(4) if ree[i] != a[i]])) for x in "".join(set([ree[i] for i in range(4) if ree[i] != a[i]]))) == c: # first criteria and second criteria respectively
                    raise
            correct.append(ree)
        except Exception:
            pass
    if correct:
        if len(correct) == 1:
            print(correct[0])
        else:
            print("indeterminate")
    else:
        print("impossible")