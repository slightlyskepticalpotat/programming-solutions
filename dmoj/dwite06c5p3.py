for _ in range(5):
    code = input().strip()
    check = 10 - sum([int(code[i]) if i % 2 else int(code[i]) * 3 for i in range(len(code) - 1)]) % 10
    print(code[:-1] + str(check))