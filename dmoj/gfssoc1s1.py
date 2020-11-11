import functools, operator

friends = [[int(i) for i in input().split()][1:] for _ in range(int(input()))]
friends = sorted([[i + 1, functools.reduce(operator.mul, friends[i])] for i in range(len(friends))], key = lambda x: x[1], reverse = True)
print("\n".join([str(friend[0]) for friend in friends[:3]]))