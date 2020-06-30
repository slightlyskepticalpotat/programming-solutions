def binary(goal, minimum, maximum):
    tries = 0
    while minimum <= maximum:
        tries+=1
        guess = (minimum + maximum)//2
        if goal == guess:
            return tries
        elif goal > guess:
            minimum = guess
        elif goal < guess:
            maximum = guess
goal, minimum, maximum = map(int, input().split())
print(binary(goal, minimum, maximum))