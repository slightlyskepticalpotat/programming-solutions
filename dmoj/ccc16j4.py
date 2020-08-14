hours, minutes = map(int, input().strip().split(":"))
time, distance = 60 * hours + minutes, 240 # integers are the devil's work

while distance > 0:
    if 420 <= time < 600 or 900 <= time < 1140:
        distance -= 1
    else:
        distance -= 2
    time += 1
hours, minutes = divmod(time, 60)
print(f"{str(hours % 24).zfill(2)}:{str(minutes).zfill(2)}")