for _ in range(int(input())):
  if "".join(sorted([char for char in input().strip()])) == "abcdefghijklmnopqrstuvwxyz":
      print("OK.")
  else:
      print("Nope.")