# https://dmoj.ca/problem/lcs
# pg 185
import sys
input = sys.stdin.readline
placeholder = input()
n = [int(i) for i in input().strip().split()]
m = [int(i) for i in input().strip().split()]

def lcs(list1, list2):
    list1_len = len(list1)+1
    list2_len = len(list2)+1
    values = [[None]*(list2_len) for i in range(list1_len)]
    
    for i in range(list1_len):
        for j in range(list2_len):
            if i == 0 or j == 0:
                values[i][j] = 0
            elif list1[i-1] == list2[j-1]:
                values[i][j] = values[i-1][j-1]+1
            else:
                values[i][j] = max(values[i-1][j], values[i][j-1])
    return values[list1_len-1][list2_len-1]

print(lcs(n, m))