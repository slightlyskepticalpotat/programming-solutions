def is_seq(x):
    elements = [int(i) for i in list(str(x))]
    for i in range(len(elements) - 1):
        if not elements[i+1] - elements[i] == elements[1] - elements[0]:
            return False
    return True

d = int(input())

sequences = 31 * (d // 720) # 31 sequences every 12 hours
d %= 720
hours, minutes = d // 60, d % 60
if hours > 0:
    for i in range(12, 13 + hours): # leftover time
        for j in range(60):
            if i == 12 + hours and j > minutes:
                break
            if j >= 10: # double digits
                if i == 12: # 12 hour clock dumb
                    if is_seq(str(i) + str(j)):
                        sequences += 1
                else:
                    if is_seq(str(i % 12) + str(j)):
                        sequences += 1
            else:
                if i == 12: # 12 hour clock dumb
                    if is_seq(str(i) + "0" + str(j)):
                        sequences += 1
                else:
                    if is_seq(str(i % 12) + "0" + str(j)):
                        sequences += 1
else:
    for j in range(minutes + 1):
        if j >= 10:
            if is_seq("12" + str(j)):
                sequences+=1
        else:
            if is_seq("12" + "0" + str(j)):
                sequences+=1
print(sequences)