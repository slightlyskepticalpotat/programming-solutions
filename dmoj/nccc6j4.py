import sys
input = sys.stdin.readline

freq = {"Deluxe Tuna Bitz": 0, "Bonito Bitz": 0, "Sashimi": 0, "Ritzy Bitz": 0}
answers = []
for i in range(int(input())):
    freq[input().strip()]+=1
for thing in freq.keys():
    if freq[thing] != 0:
        answers.append([thing, freq[thing]])
answers.sort(key=lambda x: x[1], reverse=True)
answers.sort(key=lambda x: freq.keys())
for thing in answers:
    print(*thing)