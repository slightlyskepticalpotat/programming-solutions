import itertools

letters = list(map(''.join, itertools.product("abcdefghijklmnopqrstuvwxyz", repeat = 1))) + list(map(''.join, itertools.product("abcdefghijklmnopqrstuvwxyz", repeat = 2))) + list(map(''.join, itertools.product("abcdefghijklmnopqrstuvwxyz", repeat = 3)))

w = int(input())
print(*letters[:w])