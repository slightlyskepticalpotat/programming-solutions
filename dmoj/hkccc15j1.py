import sys
input = sys.stdin.readline

def winner(a, b):
    if a == "rock":
        if b == "rock":
            return "tie"
        elif b == "paper":
            return "b"
        elif b == "scissors":
            return "a"
    elif a == "paper":
        if b == "rock":
            return "a"
        elif b == "paper":
            return "tie"
        elif b == "scissors":
            return "b"
    elif a == "scissors":
        if b == "rock":
            return "b"
        elif b == "paper":
            return "a"
        elif b == "scissors":
            return "tie"
games = int(input())
alice_wins = 0
bob_wins = 0
alice = [word for word in input().split()]
bob = [word for word in input().split()]

for i in range(len(alice)):
    result = winner(alice[i], bob[i])
    if result == "a":
        alice_wins+=1
    elif result == "b":
        bob_wins+=1
print(alice_wins, bob_wins)