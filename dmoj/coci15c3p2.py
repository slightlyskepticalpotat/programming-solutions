import random, string

min_words, max_words = map(int, input().split())
print(" ".join("".join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 15))) for j in range(random.randint(min_words, max_words))))