placeholder = input()
total = input()
total = total.lower()

count_a = int(total.count("a"))
count_b = int(total.count("b"))

if count_a > count_b:
    print("A")
elif count_b > count_a:
    print("B")
elif count_a == count_b:
    print("Tie")