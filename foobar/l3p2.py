def solution(code):
    div, mul = [0 for _ in range(len(code))], [0 for _ in range(len(code))]
    for i in range(1, len(code)):
        for j in range(i):
            if not code[i] % code[j]:
                div[i] += 1
        for j in range(i + 1, len(code)):
            if not code[j] % code[i]:
                mul[i] += 1
    return sum([div[i] * mul[i] for i in range(len(code))])
