# https://dmoj.ca/problem/lcs
# https://dmoj.ca/problem/dpf
# pg 204
n = [char for char in input().strip()]
m = [char for char in input().strip()]

def lcs(list1, list2):
    list1_len = len(list1)+1
    list2_len = len(list2)+1
    values = [[None]*(list2_len) for i in range(list1_len)]
    
    for i in range(list1_len):
        for j in range(list2_len):
            if i == 0 or j == 0: # build the dp array
                values[i][j] = 0
            elif list1[i-1] == list2[j-1]:
                values[i][j] = values[i-1][j-1]+1
            else:
                values[i][j] = max(values[i-1][j], values[i][j-1])
    return values[-1][-1], values

def print_lcs(lcs_length, array):
    if lcs_length == 0:
        return ""
    else:
        lcs = [""] * (lcs_length+1)
        i = len(n)
        j = len(m)
        while i > 0 and j > 0: # start from bottom left and traverse array
            if n[i-1] == m[j-1]: # if both letters are same, move left, up
                lcs[lcs_length-1] = n[i-1]
                i-=1
                j-=1
                lcs_length-=1
            elif array[i-1][j] > array[i][j-1]: # else, go in direction with higher value
                i-=1
            else:
                j-=1
    print("".join(lcs))
a, b = lcs(n, m)
print_lcs(a, b)