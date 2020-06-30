import sys # fast input since there might be a lot of text
input = sys.stdin.readline

a, b = map(int, input().split())
input_text, output_text, output_lines = [], [], 0
for i in range(int(input())):
    input_text.append(input().strip().split()) # each input line is split into a list of words

for thing in input_text:
    lines = [[]] # multi-line representation of original line
    for word in thing:
        line = " ".join(lines[-1])
        if len(line + word) + 1 > a: # check if the new sentence exceeds character limit
            lines.append([])
            line = " ".join(lines[-1])
        if len(line + word) + 1 <= a:
            lines[-1].append(word) # add the new word to the sentence
    output_text.append(lines)
for thing in output_text:
    output_lines += len(thing) # count number of output lines
if output_lines > b:
    print("Terminal Overflow")
else:
    for thing in output_text:
        for line in thing:
            print(" ".join(line)) # print output lines one word at a time