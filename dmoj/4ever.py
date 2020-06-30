def to_word(x):
    word = ""
    digits = {900: "ninehundred", 800: "eighthundred", 700: "sevenhundred", 600: "sixhundred", 500: "fivehundred", 400: "fourhundred", 300: "threehundred", 200: "twohundred", 100: "onehundred", 90: "ninety", 80: "eighty", 70: "seventy", 60: "sixty", 50: "fifty", 40: "forty", 30: "thirty", 20: "twenty", 19: "nineteen", 18: "eighteen", 17: "seventeen", 16: "sixteen", 15: "fifteen", 14: "fourteen", 13: "thirteen", 12: "twelve", 11: "eleven", 10: "ten", 9: "nine", 8: "eight", 7: "seven", 6: "six", 5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}
    units = {1000000000: "billion", 1000000: "million", 1000: "thousand", 100: "hundred"}
    for unit in units.keys():
        if x >= unit:
            for digit in digits.keys():
                if x // unit >= digit:
                    x -= digit*unit
                    word += digits[digit]
            word += units[unit]
    for digit in digits.keys():
        if x >= digit:
            word+= digits[digit]
            x -= digit
    return word

number = int(input())
while number != 4:
    number = len(to_word(number))
    print(number)