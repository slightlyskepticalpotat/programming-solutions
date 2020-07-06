time = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1, 'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2, 'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2, 'v': 3, 'w': 1, 'x': 2, 'y': 3, 'z': 4}
keys = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

while True:
    phrase = [char for char in input().strip()]
    time_taken = 0
    if phrase == ["h", "a", "l", "t"]:
        raise SystemExit
    for i in range(len(phrase)-1):
        for thing in keys.keys():
            if phrase[i] in keys[thing] and phrase[i+1] in keys[thing]:
                time_taken += 2
                break
        time_taken+=time[phrase[i]]
    time_taken+=time[phrase[-1]]
    print(time_taken)