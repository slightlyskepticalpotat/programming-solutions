import sys

input = sys.stdin.readline

for _ in range(int(input())):
    sentence = [char for char in input().strip() if char in "()[]{}<>"]
    open, close, flag, queue = "([{<", ")]}>", True, []
    match = dict(zip(open, close))
    try:
        for char in sentence:
            if char in open:
                queue.append(match[char])
            elif char in close:
                if not queue or char != queue.pop():
                    print("FALSE")
                    raise
        if not queue:
            print("TRUE")
        else:
            print("FALSE")
    except:
        pass