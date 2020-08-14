ree1 = [char for char in input().strip().split()]
ree2 = ree1[::-1]

print((ree1.index("L") + 1), (4 - ree2.index("R")))
print((ree1.index("R") + 1), (4 - ree2.index("L")))