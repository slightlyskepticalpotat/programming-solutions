import itertools

def solution(code):
    code.sort(reverse = True)
    for i in range(len(code), 0, -1):
        for can in itertools.combinations(code, i):
            if not sum(can) % 3:
                return int("".join([str(j) for j in can]))
    return 0
