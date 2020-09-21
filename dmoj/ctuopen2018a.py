faces = [[[":", ":", ":"], [":", "o", ":"], [":", ":", ":"]], [["o", ":", ":"], [":", ":", ":"], [":", ":", "o"]], [["o", ":", ":"], [":", "o", ":"], [":", ":", "o"]], [["o", ":", "o"], [":", ":", ":"], ["o", ":", "o"]], [["o", ":", "o"], [":", "o", ":"], ["o", ":", "o"]], [["o", ":", "o"], ["o", ":", "o"], ["o", ":", "o"]]]
image = [[char for char in input().strip()] for _ in range(3)]
for _ in range(10):
    image = [list(row) for row in zip(*image[::-1])]
    if image in faces:
        print(faces.index(image) + 1)
        raise SystemExit
print("unknown")