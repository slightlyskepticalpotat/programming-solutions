import sys
input = sys.stdin.readline

for i in range(int(input())):
    length = int(input())
    trains = [int(i) for i in input().strip().split()]
    swaps = 0
    # count inversions
    for i in range(len(trains)):
        for j in range(i+1, len(trains)):
            if trains[i] > trains[j]:
                swaps += 1
    print("Optimal train swapping takes %s swaps." % swaps)