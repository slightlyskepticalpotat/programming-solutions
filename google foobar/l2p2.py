def solution(code):
    code = [list(map(int, i.split("."))) for i in code]
    code.sort()
    return [".".join(str(j) for j in i) for i in code]
