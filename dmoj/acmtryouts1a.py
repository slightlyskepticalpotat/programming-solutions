import sys

input = sys.stdin.readline

for i in range(int(input())):
    opponent = input().strip()
    if opponent == "Rock":
        print("Paper")
    elif opponent == "Paper":
        print("Scissors")
    elif opponent == "Scissors":
        print("Rock")
    elif opponent == "Fox":
        print("Foxen")
    else:
        raise SystemExit