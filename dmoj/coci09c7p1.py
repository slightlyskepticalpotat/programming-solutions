h, m = map(int, input().split())
time = (h * 60 + m - 45) % 1440
print(*divmod(time, 60))