blasts = [int(input()) for _ in range(int(input()))]
blasts = [i if i > 0 else -i for i in blasts]
print(sum(blasts))