crossword = []
words = []
rows, columns = map(int, input().split())
for i in range(rows):
    crossword.append([char for char in input().strip()])

for i in range(len(crossword)):
    row_words = "".join(crossword[i]).split("#")
    for row_word in row_words:
        if len(row_word) >= 2:
            words.append(row_word)
crossword = list(zip(*crossword[::-1])) # rotate
crossword = list(zip(*crossword[::-1])) # rotate
crossword = list(zip(*crossword[::-1])) # rotate
for i in range(len(crossword)):
    col_words = "".join(crossword[i]).split("#")
    for col_word in col_words:
        if len(col_word) >= 2:
            words.append(col_word)
words.sort()
print(words[0])