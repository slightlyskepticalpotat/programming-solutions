n = int(input())
good_logs = [log for log in input().split("X") if log]
print(len(good_logs))
print("\n".join(good_logs))