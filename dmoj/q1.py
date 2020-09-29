import statistics

marks = [float(input()) for _ in range(int(input()))]
print(f"The median on the test is {statistics.median(marks)}")