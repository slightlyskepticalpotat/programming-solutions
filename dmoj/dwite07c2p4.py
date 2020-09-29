import sys

input = sys.stdin.readline

for _ in range(5):
    sentence = [char for char in input().strip() if char in "()[]{}"]
    open, close, flag, queue = "([{", ")]}", True, []
    match = dict(zip(open, close))
    try:
        for char in sentence:
            if char in open:
                queue.append(match[char])
            elif char in close:
                if not queue or char != queue.pop():
                    print("not balanced")
                    raise
        if not queue:
            print("balanced")
        else:
            print("not balanced")
    except:
        pass