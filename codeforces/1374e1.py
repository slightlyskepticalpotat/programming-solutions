import sys

input = sys.stdin.readline

n, k = map(int, input().split())
alice, bob, both, alice_psa, bob_psa, both_psa, best = [], [], [], [0], [0], [0], float("inf")
for _ in range(n):
    t, a, b = map(int, input().split())
    if a and b:
        both.append(t)
    elif a:
        alice.append(t)
    elif b:
        bob.append(t)

alice, bob, both = sorted(alice), sorted(bob), sorted(both)
for i in range(len(alice)):
    alice_psa.append(alice_psa[i] + alice[i])
for i in range(len(bob)):
    bob_psa.append(bob_psa[i] + bob[i])
for i in range(len(both)):
    both_psa.append(both_psa[i] + both[i])

for i in range(len(both) + 1): # common books
    if 0 <= (k - i) < min(len(alice_psa), len(bob_psa)):
        best = min(best, both_psa[i] + alice_psa[k - i] + bob_psa[k - i])
if best < float("inf"):
    print(best)
else:
    print(-1)
