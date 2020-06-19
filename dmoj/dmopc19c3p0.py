import sys
input = sys.stdin.readline

number = int(input())

for i in range(0,number):
    seq = []
    c_dif_1 = 0
    c_dif_2 = 0
    c_mul_1 = 0
    c_mul_2 = 0
    seq = list(map(int, input().split()))
    c_dif_1 = seq[1] - seq[0]
    c_dif_2 = seq[2] - seq[1]
    try:
        c_mul_1 = seq[2]/seq[1]
        c_mul_2 = seq[3]/seq[2]
    except:
        pass
    if c_dif_1 == c_dif_2 and c_mul_1 == c_mul_2:
        print('both')
    elif c_dif_1 == c_dif_2:
        print('arithmetic')
    elif c_mul_1 == c_mul_2:
        print('geometric')
    else:
        print('neither')