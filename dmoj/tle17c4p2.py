import datetime

h, m, s = map(int, input().strip().split(":"))
working = [i for i in input().strip()]
time, min_diff, best_time = h * 3600 + m * 60 + s, 362439, ""

for i in range(100):
    for j in range(100):
        for k in range(100):
            if all(i in working for i in str(i).zfill(2) + str(j).zfill(2) + str(k).zfill(2)):
                if abs(i * 3600 + j * 60 + k - time) < min_diff:
                    min_diff = abs(i * 3600 + j * 60 + k - time)
                    best_time = str(i).zfill(2) + ":" + str(j).zfill(2) + ":" + str(k).zfill(2)
print(best_time)