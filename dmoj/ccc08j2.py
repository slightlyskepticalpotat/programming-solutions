import sys
input = sys.stdin.readline
songs = ["A", "B", "C", "D", "E"]
while True:
    button = int(input())
    times = int(input())
    if button == 4 and times == 1:
        print(*songs)
        break
    else:
        for i in range(times):
            if button == 1:
                songs.append(songs.pop(0))
            if button == 2:
                songs.insert(0, songs.pop(-1))
            if button == 3:
                songs[0], songs[1] = songs[1], songs[0]