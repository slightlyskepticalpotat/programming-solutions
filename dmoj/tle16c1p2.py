import statistics, sys

input = sys.stdin.readline

boxes = [int(int(input())) for _ in range(int(input()))]
print(len([box for box in boxes if box <= min(statistics.mean(boxes), min(statistics.median(boxes), statistics.mean(statistics.multimode(boxes))))]))