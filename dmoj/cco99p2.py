import collections, sys
input = sys.stdin.readline

def most(text, position):
    counter = collections.Counter(text)
    try:
        most_words = sorted(counter.values())[-position]
        if most_words == sorted(counter.values())[-position+1] and most_words < k: # check for invalid value but duplicate counter
            return ""
    except: # not found
        return ""
    return "\n".join([word for word, count in counter.items() if count == most_words]) + "\n"

def to_ordinal(x):
    suffix = ["th", "st", "nd", "rd", "th"][min(x % 10, 4)] # tries to determine based on unit
    if 11 <= x % 100 <= 13: # checks hundreds digit
        suffix = "th"
    return str(x) + suffix
    
for i in range(int(input())):
    text = []
    m, k = map(int, input().split())
    for i in range(m):
        text.append(input().strip())
    print("{} most common word(s):".format(to_ordinal(k)))
    print(most(text, k))