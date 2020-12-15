prefs = [input().strip() for _ in range(int(input()))]
if prefs.count("cats") > prefs.count("dogs"):
    print("cats")
elif prefs.count("dogs") > prefs.count("cats"):
    print("dogs")
else:
    print("equal")