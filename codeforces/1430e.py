import sys

input = sys.stdin.readline

def inversions(x): # actually does merge sort
    if len(x) == 1:
        return x, 0
    a, b, both = x[:len(x) // 2], x[len(x) // 2:], []
    a, a_inv = inversions(a)
    b, b_inv = inversions(b)
    inv, i, j = a_inv + b_inv, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            both.append(a[i])
            i += 1
        else:
            both.append(b[j])
            j += 1
            inv += len(a) - i
    both += a[i:]
    both += b[j:]
    return both, inv

n, s, pos, swaps = int(input()), input().strip()[::-1], {i: [] for i in range(26)}, 0
for i in range(n): # order of elements in new array
    pos[ord(s[i]) - ord("a")].append(i)
order = [pos[ord(s[i]) - ord("a")].pop() for i in range(n)][::-1]
print(inversions(order)[1])
