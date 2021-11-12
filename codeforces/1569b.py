import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, s = int(input()), input().strip()
    if s.count("1") in [n - 1, n - 2]:
        print("NO")
    else:
        print("YES")
        results, wins = [[""] * n for i in range(n)], [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    results[i][j] = "X"
                if not results[i][j]:
                    if s[i] == "1" or s[j] == "1":
                        results[i][j] = "="
                        results[j][i] = "="
                    elif s[i] == "2" and s[j] == "2":
                        if not wins[i]:
                            wins[i] += 1
                            results[i][j] = "+"
                            results[j][i] = "-"
                        else:
                            results[i][j] = "-"
                            results[j][i] = "+"
        print("\n".join(["".join(i) for i in results]))
