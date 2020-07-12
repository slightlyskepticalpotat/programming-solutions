area_code, number = input().split()
if len(number) != 7 or len(area_code) != 3 or area_code not in ["416", "647", "437"]: # leading 0
    print("invalid")
elif area_code == "416":
    print("valuable")
else:
    print("valueless") # ;-;