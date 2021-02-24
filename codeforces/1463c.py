import sys

input = sys.stdin.readline

for _ in range(int(input())):
    commands = [[int(i) for i in input().split()] for j in range(int(input()))] # time, destination
    commands.append([float("inf"), 0])
    position, direction, dist_left, successful, to_move = 0, 0, 0, 0, 0
    for i in range(len(commands) - 1):
        next = commands[i + 1][0]
        if not dist_left:
            dist_left = abs(position - commands[i][1])
            if commands[i][-1] > position:
                direction = 1
            else:
                direction = -1
        to_move = min(dist_left, next - commands[i][0])
        if min(position, position + direction * to_move) <= commands[i][1] <= max(position, position + direction * to_move):
            successful += 1
        position += direction * to_move
        dist_left -= to_move
    print(successful)
