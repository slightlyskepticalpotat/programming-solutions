# https://dmoj.ca/problem/dmopc14c4p4

import sys
input = sys.stdin.readline

message, candidates = input().strip(), set()

candidates = set([message[i:i+9] for i in range(len(message) - 8)])

if candidates: # stopping the program early
    for i in range(int(input())):
        key = input().strip()
        if "HAILHYDRA".translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key)) in candidates:
            print(message.translate(str.maketrans(key, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")))
            raise SystemExit
print("KeyNotFoundError")