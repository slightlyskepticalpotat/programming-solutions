from collections import deque
diff = [int(i) for i in input().strip().split()]
for i in range(len(diff)+1):
    res = deque()
    flag = 0 
    for j in range(len(diff)+1):
        if j == i:
            res.append(0)
            flag = 1
        else:
            if flag == 0:
                res.append(sum(diff[j:i]))
            if flag == 1:
                res.append(sum(diff[i:j]))
            
    print(*res)