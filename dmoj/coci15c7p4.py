import sys

input = sys.stdin.readline

def recurse(resistor):
    if len(resistor) == 1:
        return values[int(resistor) - 1]
    buf, level, res, invert = "", 0, 0, -1
    for i in range(1, len(resistor) - 1):
        if resistor[i] in ["|", "-"] and not level:
            if invert == -1:
                if resistor[i] == "|":
                    invert = True
                else:
                    invert = False
            if invert:
                res += 1 / recurse(buf)
            else:
                res += recurse(buf)
            buf = ""
        elif resistor[i] == "(":
            level += 1
            buf += resistor[i]
        elif resistor[i] == ")":
            level -= 1
            buf += resistor[i]
        else:
            buf += resistor[i]
    if invert:
        res += 1 / recurse(buf)
        res = 1 / res
    else:
        res += recurse(buf)
    return res

n, values = int(input()), [float(i) for i in input().split()]
line = input().strip().replace("R", "")
print(recurse(line))