import sys

input = sys.stdin.readline

laziness = list(sorted([int(input()) for _ in range(int(input()))]))
difficulty = list(reversed(laziness))
print(sum([laziness[i] * difficulty[i] for i in range(len(laziness))]) % 10007)