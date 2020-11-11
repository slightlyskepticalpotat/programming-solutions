import re, sys

input = sys.stdin.readline

def convert(x):
    x = x.lower()
    pivot = x.find("@")
    x = x[:pivot].replace(".", "") + x[pivot:]
    x = re.sub(r'\+.*(?=@)', "", x)
    return x

for i in range(10):
    addresses = [input().strip() for i in range(int(input()))]
    addresses = map(convert, addresses)
    print(len(set(addresses)))