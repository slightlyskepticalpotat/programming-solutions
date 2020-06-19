import sys
input = sys.stdin.readline

number = input()
blocks = list(input().split())
blocks = [int(i) for i in blocks]

def bubble_sort(x):
    format_print(x)
    while True:
        swapped = 0
        for i in range(0, len(x)-1):
            if x[i+1] < x[i]:
                x[i+1], x[i] = x[i], x[i+1]
                swapped = 1
                format_print(x)
        if swapped == 0:
            break
def format_print(x):
    for thing in x:
        print(thing, end=" ")
    print("")
        
bubble_sort(blocks)