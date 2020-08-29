# O-, O+, A-, A+, B-, B+, AB-, AB+ == 0, 1, 2, 3, 4, 5, 6, 7
# https://www.blood.ca/sites/default/files/styles/max_650x650/public/2018-09/DonorRecipient-Chart_1.jpg

compatible = {0: [0], 1: [1, 0], 2: [2, 0], 3: [1, 2, 3, 0], 4: [4, 0], 5: [1, 4, 5, 0], 6: [2, 4, 6, 0], 7: [1, 2, 3, 4, 5, 6, 7, 0]} # O- is the universal donor
donors = [int(i) for i in input().split()]
patients = [int(i) for i in input().split()]
transfusions = 0

for patient in compatible.keys():
    for donor in compatible[patient]:
        current = min(donors[donor], patients[patient])
        transfusions += current
        donors[donor] -= current
        patients[patient] -= current
print(transfusions)