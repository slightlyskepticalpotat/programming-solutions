import sys

input = sys.stdin.readline

s = input().strip()
words, i, word = [], 0, ""
while i < len(s):
    word = s[i]
    i += 1
    if word == "A":
        while i < len(s):
            if s[i] != "A":
                word += s[i]
                i += 1
            else:
                break
            if i == len(s):
                break
            if s[i] == "A":
                word += s[i]
                i += 1
            else:
                break
    else:
        while i < len(s):
            if s[i] == "A":
                word += s[i]
                i += 1
            else:
                break
            if i == len(s):
                break
            if s[i] != "A":
                word += s[i]
                i += 1
            else:
                break
    words.append(word)
print(*words)
