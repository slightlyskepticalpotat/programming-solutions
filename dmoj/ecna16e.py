import sys
input = sys.stdin.readline
string = input().strip()
substrings = []
longest = 99999
longest_index = 0

for i in range(0, len(string)):
    for j in range(i+1, len(string)):
        substrings.append(string[i:j])
for thing in substrings:
    yeet = string.replace(thing, "M")
    if (len(yeet) + len(thing)) < longest:
        longest = (len(yeet) + len(thing))
if len(string) < longest:
    print(len(string))
else:
    print(longest)