for _ in range(int(input())):
    n, q = map(int, input().split())
    values, dp_ones, dp_twos = [int(i) for i in input().split()], [-float("inf")], [0] # maximum value of odd, maximum value of even
    for i in range(n):
        dp_ones.append(max(dp_ones[-1], dp_twos[-1] + values[i]))
        dp_twos.append(max(dp_twos[-1], dp_ones[-1] - values[i]))
    print(max(dp_ones[-1], dp_twos[-1]))
