from fractions import Fraction

for _ in range(5):
    n1, d1, n2, d2 = map(int, input().split())
    line = str(Fraction(n1, d1) + Fraction(n2, d2))
    print(line.replace("/", " "))