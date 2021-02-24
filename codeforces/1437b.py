for _ in range(int(input())):
    n, string = int(input()), input().strip()
    zero_count, one_count = sum([string[i:i+2] == "00" for i in range(n - 1)]), sum([string[i:i+2] == "11" for i in range(n - 1)])
    print(max(zero_count, one_count)) # flips
