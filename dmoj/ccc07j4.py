one = sorted([char for char in input().replace(" ", "")])
two = sorted([char for char in input().replace(" ", "")])
if one == two:
    print("Is an anagram.")
else:
    print("Is not an anagram.")