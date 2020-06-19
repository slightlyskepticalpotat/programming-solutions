# https://dmoj.ca/problem/ccc03s4
# suffix array https://en.wikipedia.org/wiki/Suffix_array

def largest_common_prefix(first, second): # filter out duplicate substrings
    for i in range(min(len(first), len(second))):
        if first[i:i+1] != second[i:i+1]: # where they first differ
            return i
    return min(len(first), len(second))

for i in range(int(input())):
    string = input().strip()
    suffix = []
    for i in range(len(string)):
        suffix.append(string[i:]) # build the suffix array
    suffix.sort()

    counter = len(suffix[0]) + 1 # string[:i] for i in len(string)
    for i in range(1, len(suffix)):
        counter = counter + len(suffix[i]) - largest_common_prefix(suffix[i], suffix[i-1])
        # add the number of prefixes of the suffix (length), subtract duplicates
    print(counter)