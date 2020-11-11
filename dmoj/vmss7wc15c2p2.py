# manacher's algorithm

import sys

input = sys.stdin.readline

def longest_pal(x):
    x = "".join(["#" + char for char in x] + ["#"])
    longest = [0 for _ in range(len(x))]
    centre, right = 0, 0 # mfw american politics
    for i in range(len(x)):
        opposite = 2 * centre - i # find the mirror image
        if right > i:
            longest[i] = min(right - i, longest[opposite])
        else:
            longest[i] = 0
        try:
            while x[i + 1 + longest[i]] == x[i - 1 - longest[i]]: # extend around the centre
                longest[i] += 1
        except:
            pass
        if i + longest[i] > right: # slide to the right
            centre, right = i, i + longest[i]
    centre, right = longest.index(max(longest)), max(longest)
    return x[centre - right:centre + right].replace("#", "")

n = int(input())
result = longest_pal(input().strip())
print(result)
print(len(result))