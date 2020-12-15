import sys

input = sys.stdin.readline

while True:
    line = float(input())
    if not line:
        break
    base, exp = f"{line:.3E}".split("E")
    if int(exp):
        print(f"{base} x 10^{int(exp)}")
    else:
        print(base)