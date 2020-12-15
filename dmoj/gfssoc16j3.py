import sys

input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    words = [i for i in input().split()]
    for i in range(n):
        words[i] = words[i].replace(".", "!!!")
    for i in range(n):
        if words[i].isupper():
            words[i] = "!!!" + words[i] + "!!!"
    print(" ".join(word for word in words))