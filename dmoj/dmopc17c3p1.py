import sys
input = sys.stdin.readline

number = int(input())
tests = [int(i) for i in input().split()]

print(min(tests))