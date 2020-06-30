import sys
input = sys.stdin.readline

for i in range(int(input())):
     stuff = [char.lower() for char in input().strip()]
     output = []
     for thing in stuff:
          if thing == "a":
               output.append("Hi!")
          elif thing == "e":
               output.append("Bye!")
          elif thing == "i":
               output.append("How are you?")
          elif thing == "o":
               output.append("Follow me!")
          elif thing == "u":
               output.append("Help!")
          elif thing.isnumeric():
               output.append("Yes!")
     print(*output)