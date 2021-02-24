for _ in range(int(input())):
    px, py = map(int, input().split())
    directions = [char for char in input().strip()]
    if px >= 0 and py >= 0:
        if directions.count("R") >= px and directions.count("U") >= py:
            print("YES")
        else:
            print("NO")
    elif px >= 0 and py <= 0:
        if directions.count("R") >= px and directions.count("D") >= abs(py):
            print("YES")
        else:
            print("NO")
    elif px <= 0 and py >= 0:
        if directions.count("L") >= abs(px) and directions.count("U") >= py:
            print("YES")
        else:
            print("NO")
    elif px <= 0 and py <= 0:
        if directions.count("L") >= abs(px) and directions.count("D") >= abs(py):
            print("YES")
        else:
            print("NO")
