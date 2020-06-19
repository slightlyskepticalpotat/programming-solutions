import sys, collections
input = sys.stdin.readline
cases = int(input())
readings = []

for i in range(cases):
    readings.append(int(input()))
    
freqs = collections.Counter(readings).most_common()
highest = 0
highest_freq = freqs[1][1]

if freqs[0][1] != freqs[1][1]:
    for i in range(len(freqs)):
        if abs(freqs[0][0]-freqs[i][0]) > highest and freqs[i][1] == highest_freq:
            highest = abs(freqs[0][0]-freqs[i][0])
    print(highest)
else:
    for i in range(len(freqs)):
        for j in range(len(freqs)):
            if abs(freqs[i][0]-freqs[j][0]) > highest and freqs[i][1] == highest_freq and freqs[j][1] == highest_freq:
                highest = abs(freqs[i][0]-freqs[j][0])
    print(highest)