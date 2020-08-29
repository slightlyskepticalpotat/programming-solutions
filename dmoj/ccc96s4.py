import sys

input = sys.stdin.readline

convert = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
backwards = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

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

def int_to_rom(x):
    roman = ""
    for key in backwards.keys():
        while key <= x:
            roman = roman + backwards[key]
            x -= key
    return roman

for i in range(int(input())):
    line = input().strip()
    a, b = line.replace("=", "").split("+")
    result =  rom_to_int(a) + rom_to_int(b)
    if result <= 1000:
        print(line + int_to_rom(result))
    else:
        print(line + "CONCORDIA CUM VERITATE")