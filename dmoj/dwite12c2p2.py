def to26(x):
    x = [l_to_n[i] for i in x][::-1]
    result = 0
    for i in range(len(x)):
        result += x[i] * 26 ** i
    return result

def from26(x):
    result = []
    while x:
        result.append(int(x % 26))
        x //= 26
    return result[::-1]

l_to_n = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
n_to_l = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

for _ in range(5):
    a, b = input().strip().lower().split()
    a, b = [char for char in a], [char for char in b]
    n = from26(to26(a) + to26(b))
    print("".join([n_to_l[i] for i in n]).upper())