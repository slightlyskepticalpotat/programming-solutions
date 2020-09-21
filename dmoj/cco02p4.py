distance = int(input())
competitors = [[float(i) for i in input().split()] for i in range(int(input()) - 1)]
cheater = [float(i) for i in input().split()]
best_time = 0
best_r = float("inf")
best_k = float("inf")

for i in range(distance * 512): # change this for precision/speed
    r = i / 512
    k = distance - r
    min_time = float("inf")
    for competitor in competitors:
        time = r / competitor[0] + k / competitor[1]
        if time < min_time:
            min_time = time
    cheater_time = r / cheater[0] + k / cheater[1]
    if cheater_time <= min_time and min_time - cheater_time >= best_time: # tie
        best_time = min_time - cheater_time
        best_r = r
        best_k = k
if best_time == 0 and best_r == float("inf") and best_k == float("inf"):
    print("The cheater cannot win.")
else:
    print(f"The cheater can win by {round(best_time * 3600)} seconds with r = {round(best_r, 2):.2f}km and k = {round(best_k, 2):.2f}km.")