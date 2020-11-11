# https://brilliant.org/wiki/rectangular-grid-walk-no-restriction/#restrictions
# counting problems are cancer

modulo = 1000000007

def factorial(x):
    for i in range(2, x):
        x = x * i % modulo
    return x

def combination(n, k):
    return factorial(n) * pow(factorial(n - k), modulo - 2, modulo) * pow(factorial(k), modulo - 2, modulo) % modulo # fermat's little theorem

w, h, x = map(int, input().split())
w, h = w - 1, h - 1 # adjust for start at (1, 1)
blocks = tuple(sorted((tuple(int(i) - 1 for i in input().split()) for _ in range(x)), key = lambda x: x[0])) # left to right

if x == 0:
    print(combination(w + h, h) % modulo)
elif x == 1:
    a, b = blocks[0][0], blocks[0][1]
    print((combination(w + h, h) - combination(a + b, b) * combination((w + h) - (a + b), h - b)) % modulo)
else:
    a1, b1, a2, b2 = blocks[0][0], blocks[0][1], blocks[1][0], blocks[1][1]
    paths = combination(w + h, h) # principle of inclusion-exclusion
    paths -= combination(a1 + b1, b1) * (combination((w + h) - (a1 + b1), (h - b1)))
    paths -= combination(a2 + b2, b2) * (combination((w + h) - (a2 + b2), (h - b2)))
    if b1 <= b2: # bottom to top
        paths += combination(a1 + b1, b1) * combination((a2 - a1) + (b2 - b1), b2 - b1) * combination(w - a2 + h - b2, h - b2)
    print(paths % modulo)