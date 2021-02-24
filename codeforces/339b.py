n, m = map(int, input().split())
tasks, time = [1] + [int(i) for i in input().split()], 0
for i in range(1, m + 1):
    if tasks[i] >= tasks[i - 1]:
        time += tasks[i] - tasks[i - 1]
    else:
        time += n - abs(tasks[i] - tasks[i - 1])
print(time)
