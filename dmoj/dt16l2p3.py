for i in range(int(input())):
  print("".join([char if char in ["0", "1"] else "0" for char in input().strip()]))