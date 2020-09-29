import sys

input = sys.stdin.readline

convert = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

def rom_to_int(x):
    x = [char for char in x]
    integer = 0
    while x:
        if len(x) >= 2:
            if x[0] + x[1] in convert.keys():
                integer += convert[x[0] + x[1]]
                x.remove(x[0])
                x.remove(x[0])
            else:
                integer += convert[x[0]]
                x.remove(x[0])
        else:
            integer += convert[x[0]]
            x.remove(x[0])
    return integer

for i in range(5):
    print(rom_to_int(input().strip()))