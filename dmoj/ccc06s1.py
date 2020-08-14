import sys
input = sys.stdin.readline

genotype_1, genotype_2, phenotype = input().strip(), input().strip(), [[], [], [], [], []]
genotype_1 = [genotype_1[i:i+2] for i in range(0, len(genotype_1), 2)]
genotype_2 = [genotype_2[i:i+2] for i in range(0, len(genotype_2), 2)]
for i in range(5):
    if genotype_1[i].isupper(): # AA
        if genotype_2[i].isupper(): # AA
            phenotype[i].append(genotype_1[i][:1].upper())
        elif genotype_2[i].islower(): # aa
            phenotype[i].append(genotype_1[i][:1].upper())
        else: # Aa
            phenotype[i].append(genotype_1[i][:1].upper())
    elif genotype_1[i].islower(): # aa
        if genotype_2[i].isupper(): # AA
            phenotype[i].append(genotype_1[i][:1].upper())
        elif genotype_2[i].islower(): # aa
            phenotype[i].append(genotype_1[i][:1].lower())
        else: # Aa
            phenotype[i].append(genotype_1[i][:1].upper())
            phenotype[i].append(genotype_1[i][:1].lower())
    else: # Aa
        if genotype_2[i].isupper(): # AA
            phenotype[i].append(genotype_1[i][:1].upper())
        elif genotype_2[i].islower(): # aa
            phenotype[i].append(genotype_1[i][:1].upper())
            phenotype[i].append(genotype_1[i][:1].lower())
        else: # aa
            phenotype[i].append(genotype_1[i][:1].upper())
            phenotype[i].append(genotype_1[i][:1].lower())

for _ in range(int(input())):
    fly = [char for char in input().strip()]
    try:
        for i in range(len(fly)):
            if fly[i] not in phenotype[i]:
                print("Not their baby!")
                raise
        print("Possible baby.")
    except:
        pass