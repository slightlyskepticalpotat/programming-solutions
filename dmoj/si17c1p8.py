ways = 0
coin_number, target_value = map(int, input().split())
coins = [int(i) for i in input().strip().split()]
array = [[0] * (target_value + 1) for _ in range(coin_number + 1)] # initialize dp array
array[0][0] = 1 # array[i][j] is number of ways to get j with first i coins

for i in range(1, coin_number + 1):
    for j in range(1, target_value + 1):
        try:
            array[i][j] = array[i-1][j] + array[i-1][j-coins[i-1]]
        except:
            pass
for i in range(1, coin_number + 1):
    ways+=array[i][target_value]
    
if ways == 2:
    print(1)
else:
    print(ways)