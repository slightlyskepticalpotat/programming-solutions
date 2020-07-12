songs = []
listened = 0
for i in range(int(input())):
    minutes, seconds = map(int, input().split())
    songs.append(minutes * 60 + seconds)
max_minutes, max_seconds = map(int, input().split())
songs.sort()
max = max_minutes * 60 + max_seconds

for thing in songs:
    if max - thing >= 0:
        max -= thing
        listened+=1
print(listened)