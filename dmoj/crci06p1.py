import sys

input = sys.stdin.readline

n, max_song = int(input()), 0
songs = [[] for _ in range(n)]
for i in range(int(input())):
    present = [int(i) for i in input().split()][1:]
    if 1 in present:
        max_song += 1
        songs = [songs[i] + [max_song] if i + 1 in present else songs[i] for i in range(n)] # new song
    else:
        present.append(1) # the bard always knows
        common = list(set().union(*[songs[i] for i in range(n) if i + 1 in present])) # common songs
        songs = [common if i + 1 in present else songs[i] for i in range(n)] # swap songs
print("\n".join(sorted([str(i + 1) for i in range(n) if len(songs[i]) == max_song], key = lambda x: int(x))))