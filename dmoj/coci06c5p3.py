import sys

input = sys.stdin.readline

p1, p2 = input().strip().split()
for _ in range(int(input())):
    valid = True
    try:
        tennis = [[int(i) for i in j.split(":")] for j in input().strip().split()]
        if p1 == "federer": # he can't lose
            if any([i[0] < i[1] for i in tennis]):
                valid = False
        elif p2 == "federer":
            if any([i[1] < i[0] for i in tennis]):
                valid = False
        if min([max(i) for i in tennis]) < 6: # fastest win in 6 games
            valid = False
        if len(tennis) > 3 or len(tennis) < 2: # maximum games possible
            valid = False
        p1_games = sum([i[0] > i[1] for i in tennis])
        p2_games = sum([i[1] > i[0] for i in tennis])
        if (min(p1_games, p2_games), max(p1_games, p2_games)) in [(0, 0), (0, 1), (1, 1), (0, 3)]: # invalid set results
            valid = False
        if max(tennis[0]) > 7 or max(tennis[1]) > 7: # win condition in early sets
            valid = False
        if any([max(i) >= 7 and abs(i[0] - i[1]) > 2 for i in tennis[:2]]): # double check earlier games
            valid = False
        if any([abs(i[0] - i[1]) < 2 for i in tennis[2:]]): # win condition in later sets
            valid = False
        if len(tennis) == 3 and [7, 7] == tennis[1]: # don't get a tie if this happens
            valid = False
        if abs(tennis[0][0] - tennis[0][1]) >= 2 and [6, 6] == tennis[1]:
            valid = False
    except Exception as e:
        valid = False
    if valid:
        print("da")
    else:
        print("ne")