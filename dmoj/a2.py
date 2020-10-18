print("Ready")
while True:
    text = input()
    if not text.strip():
        break
    elif text in ["bd", "db", "pq", "qp"]:
        print("Mirrored pair")
    else:
        print("Ordinary pair")