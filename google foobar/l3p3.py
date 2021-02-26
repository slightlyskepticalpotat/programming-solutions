def solution(m, f):
    m, f, gen = int(m), int(f), 0
    while m > 1 and f > 1:
        cur = divmod(max(m, f), min(m, f))
        if not cur[1]:
            return "impossible"
        gen += cur[0]
        m, f = cur[1], min(m, f)
    return str(gen + max(m, f) - 1)
