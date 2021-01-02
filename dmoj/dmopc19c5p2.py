import sys, time

input = sys.stdin.readline
n, h = map(int, input().split())
charlie_health, bot_health = h, h
charlie_actions = [[i for i in input().strip().split()] for _ in range(n)]
bot_actions = [[i for i in input().strip().split()] for _ in range(n)]

for i in range(n):
    if bot_health <= 0:
        print("VICTORY")
        sys.exit()
    elif charlie_health <= 0:
        print("DEFEAT")
        sys.exit()
    if charlie_actions[i][0] == "A":
        if i == 0 or bot_actions[i - 1][0] != "D":
            bot_health -= int(charlie_actions[i][1])
            if bot_health <= 0:
                print("VICTORY")
                sys.exit()
        if bot_actions[i][0] == "A":
            charlie_health -= int(bot_actions[i][1])
            if charlie_health <= 0:
                print("DEFEAT")
                sys.exit()
    elif charlie_actions[i][0] == "D":
        if i != 0 and bot_actions[i - 1][0] == "D":
            bot_health -= int(bot_actions[i - 1][1])
            if bot_health <= 0:
                print("VICTORY")
                sys.exit()
        if bot_actions[i][0] == "D":
            charlie_health -= int(charlie_actions[i][1])
            if charlie_health <= 0:
                print("DEFEAT")
                sys.exit()
    if bot_health <= 0:
        print("VICTORY")
        sys.exit()
    elif charlie_health <= 0:
        print("DEFEAT")
        sys.exit()
if bot_actions[n - 1][0] == "D":
    bot_health -= int(bot_actions[n - 1][1])
    if bot_health <= 0:
        print("VICTORY")
        sys.exit()
print("TIE")