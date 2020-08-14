import sys
input = sys.stdin.readline

def last(x):
    x = x[::-1]
    answer = ""
    for char in x:
        if char in ["a", "e", "i", "o", "u"]:
            answer += char
            break
        else:
            answer += char
    return answer[::-1]

for _ in range(int(input())):
    poem = []
    for _ in range(4):
        poem.append([char for char in input().strip().split()][-1].lower())
    if last(poem[0]) == last(poem[1]) == last(poem[2]) == last(poem[3]):
        print("perfect")
    elif last(poem[0]) == last(poem[1]) and last(poem[2]) == last(poem[3]):
        print("even")
    elif last(poem[0]) == last(poem[2]) and last(poem[1]) == last(poem[3]):
        print("cross")
    elif last(poem[0]) == last(poem[3]) and last(poem[1]) == last(poem[2]):
        print("shell")
    else:
        print("free")