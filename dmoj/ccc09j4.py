width = int(input())
words = "WELCOME TO CCC GOOD LUCK TODAY".split()

while True:
    line = [] # one line
    while len(words) >= 1 and len(".".join(line + [words[0]])) <= width: # extend line
        line.append(words[0])
        del(words[0])
    if not line: # check that we have stuff to print
        break
    while len("".join(line)) < width:
        for i in range(len(line) - 1): # pad full lines
            line[i] = line[i] + "."
            if len("".join(line)) == width: # pad part lines
                break
        if len(line) == 1: # one word in line
            line[0] = line[0] + "." * (width - len(line[0]))
    print("".join(line))