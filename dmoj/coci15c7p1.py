import sys

input = sys.stdin.readline

def preprocess(x):
    processed = []
    for char in x:
        if char == "{" or char == "}":
            processed.append(char)
            processed.append("")
        elif char == ",":
            processed.append("")
        else:
            processed[-1] += char
    return processed

line, spaces = preprocess(input().strip()), 0
for i in range(len(line)):
    if line[i] == "{":
        print(" " * spaces + line[i])
        spaces += 2
    elif line[i] == "}":
        spaces -= 2
        if i + 2 < len(line) and line[i + 1] == "" and line[i + 2] != "}":
            print(" " * spaces + line[i] + ",")
        else:
            print(" " * spaces + line[i])
    elif line[i]:
        if line[i + 1] == "}":
            print(" " * spaces + line[i])
        else:
            print(" " * spaces + line[i] + ",")
    else:
        pass