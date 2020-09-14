smallest = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
word = input().strip()

for i in range(1, len(word)):
    for j in range(i + 1, len(word)):
        a, b, c = word[:i][::-1], word[i:j][::-1], word[j:][::-1]
        if a + b + c < smallest:
            smallest = a + b + c
print(smallest)