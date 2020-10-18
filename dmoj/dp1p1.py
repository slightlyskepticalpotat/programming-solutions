import sys
input = sys.stdin.readline

def max_non_adjacent(x):
    including, excluding = 0, 0 # max sum including the previous element, max sum without previous element
    for thing in x:
        temporary = max(including, excluding) # maximum sum excluding current element, since they can't be adjacent
        including = excluding + thing # update array
        excluding = temporary 
    return max(including, excluding)

numbers = []
for i in range(int(input())):
    numbers.append(int(input()))
print(max_non_adjacent(numbers))