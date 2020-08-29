def column(x):
    return [line[x] for line in numbers]

positions = {0: [4, 4], 1: [5, 4], 2: [5, 5], 3: [4, 5], 4: [3, 5], 5: [3, 4], 6: [3, 3], 7: [4, 3], 8: [5, 3], 9: [6, 3], 10: [6, 4], 11: [6, 5], 12: [6, 6], 13: [5, 6], 14: [4, 6], 15: [3, 6], 16: [2, 6], 17: [2, 5], 18: [2, 4], 19: [2, 3], 20: [2, 2], 21: [3, 2], 22: [4, 2], 23: [5, 2], 24: [6, 2], 25: [7, 2], 26: [7, 3], 27: [7, 4], 28: [7, 5], 29: [7, 6], 30: [7, 7], 31: [6, 7], 32: [5, 7], 33: [4, 7], 34: [3, 7], 35: [2, 7], 36: [1, 7], 37: [1, 6], 38: [1, 5], 39: [1, 4], 40: [1, 3], 41: [1, 2], 42: [1, 1], 43: [2, 1], 44: [3, 1], 45: [4, 1], 46: [5, 1], 47: [6, 1], 48: [7, 1], 49: [8, 1], 50: [8, 2], 51: [8, 3], 52: [8, 4], 53: [8, 5], 54: [8, 6], 55: [8, 7], 56: [8, 8], 57: [7, 8], 58: [6, 8], 59: [5, 8], 60: [4, 8], 61: [3, 8], 62: [2, 8], 63: [1, 8], 64: [0, 8], 65: [0, 7], 66: [0, 6], 67: [0, 5], 68: [0, 4], 69: [0, 3], 70: [0, 2], 71: [0, 1], 72: [0, 0], 73: [1, 0], 74: [2, 0], 75: [3, 0], 76: [4, 0], 77: [5, 0], 78: [6, 0], 79: [7, 0], 80: [8, 0], 81: [9, 0], 82: [9, 1], 83: [9, 2], 84: [9, 3], 85: [9, 4], 86: [9, 5], 87: [9, 6], 88: [9, 7], 89: [9, 8], 90: [9, 9], 91: [8, 9], 92: [7, 9], 93: [6, 9], 94: [5, 9], 95: [4, 9], 96: [3, 9], 97: [2, 9], 98: [1, 9], 99: [0, 9]}

for j in range(1):
    numbers = [["   "] * 10 for _ in range(10)]
    start, stop = int(input()), int(input())

    for i in range(start, stop + 1):
        numbers[positions[i - start][0]][positions[i - start][1]] = str(i).rjust(3, " ") # account for the fact we don't always start at 1

    numbers = [line for line in numbers if not all(number.isspace() for number in line)] # filter out empty lines
    numbers = [list(line) for line in zip(*numbers[::-1])] # rotate it
    numbers = [line for line in numbers if not all(number.isspace() for number in line)]
    numbers = [list(line) for line in zip(*numbers[::-1])]
    numbers = [list(line) for line in zip(*numbers[::-1])]
    numbers = [list(line) for line in zip(*numbers[::-1])]

    for k in range(len(numbers[0])):
        if all(len(number.strip()) <= 1 for number in column(k)): # 1 digit long column
            for line in numbers:
                if line[k][0].isspace(): # strip whitespace from column
                    line[k] = line[k][1:]

    for line in numbers:
        if line[0][0].isspace(): # strip whitespace from first element
            line[0] = line[0][1:]
        if not line[-1].isspace(): # strip whitespace from last element
            line[-1] = line[-1].rstrip()
        print("".join(line))
        # strip whitespace from last line