for _ in range(int(input())):
    s, processed = input().strip(), []
    for i in range(len(s)):
        processed.append(s[i])
        if len(processed) >= 2:
            if processed[-2] == "A" and processed[-1] == "B":
                processed.pop()
                processed.pop()
        if len(processed) >= 2:
            if processed[-2] == "B" and processed[-1] == "B":
                processed.pop()
                processed.pop()
    print(len(processed))
