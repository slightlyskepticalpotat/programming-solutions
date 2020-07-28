result = "x".join(sorted([i for i in input().split("x")]))
print(result + "\n" + str(eval(result.replace("x", "*"))))