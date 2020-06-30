# https://dmoj.ca/problem/cco07p2
import sys
input = sys.stdin.readline

def identical(a, b):
    for i in range(6):
        if a[i] != b[i]:
            return False
    return True
def rotate(x):
    rotated = []
    rotated.append(x[0:] + x[:0])
    rotated.append(x[1:] + x[:1])
    rotated.append(x[2:] + x[:2])
    rotated.append(x[3:] + x[:3])
    rotated.append(x[4:] + x[:4])
    rotated.append(x[5:] + x[:5])
    x = x[::-1]
    rotated.append(x[0:] + x[:0])
    rotated.append(x[1:] + x[:1])
    rotated.append(x[2:] + x[:2])
    rotated.append(x[3:] + x[:3])
    rotated.append(x[4:] + x[:4])
    rotated.append(x[5:] + x[:5])
    return rotated

snowflakes = {}
for i in range(int(input())):
    snowflake = [int(i) for i in input().split()]
    snowflake_value = sum(snowflake)
    if snowflake_value in snowflakes.keys():
        snowflakes[snowflake_value].append(snowflake)
    else:
        snowflakes[snowflake_value] = [snowflake]

for key in snowflakes.keys():
    for i in range(len(snowflakes[key])):
        for j in range(i+1, len(snowflakes[key])):
            for rotation in rotate(snowflakes[key][j]):
                if snowflakes[key][i] == rotation:
                    print("Twin snowflakes found.")
                    sys.exit()        
print("No two snowflakes are alike.")