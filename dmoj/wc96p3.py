provinces = ["British Columbia", "Alberta", "Saskatchewan", "Manitoba", "Ontario", "Quebec", "Nova Scotia", "Newfoundland", "New Brunswick", "PEI"]
for i in range(5):
    line = "".join([char.lower() for char in input().strip() if char.isalpha()])
    try:
        for province in provinces:
            if "".join([char.lower() for char in province if char.isalpha()]) in line:
                print(province)
                raise
        print("NO PROVINCE FOUND")
    except:
        pass