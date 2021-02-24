for _ in range(int(input())):
    x, calls, pressed = input().strip(), [], 0
    for i in range(1, 10):
        for j in range(1, 5):
            calls.append(str(i) * j)
    for call in calls:
        pressed += len(call)
        if call == x:
            break
    print(pressed)
