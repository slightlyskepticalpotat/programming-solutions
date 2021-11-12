import sys

input = sys.stdin.readline

for _ in range(int(input())):
    sudoku = [input().strip().replace("2", "1") for j in range(9)]
    print("\n".join(sudoku))