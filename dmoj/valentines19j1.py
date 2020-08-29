for i in range(int(input())):
    rating = int(input())
    if rating < 1000:
        print("Newbie")
    elif 1000 <= rating <= 1199:
        print("Amateur")
    elif 1200 <= rating <= 1499:
        print("Expert")
    elif 1500 <= rating <= 1799:
        print("Candidate Master")
    elif 1800 <= rating <= 2199:
        print("Master")
    elif 2200 <= rating <= 2999:
        print("Grandmaster")
    elif 3000 <= rating <= 3999:
        print("Target")
    elif rating > 3999:
        print("Rainbow Master")