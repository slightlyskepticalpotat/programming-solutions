import sys
input = sys.stdin.readline

atoms, bonds = map(int, input().split())
bond_map = {}
for i in range(atoms):
    bond_map[i+1] = []
for i in range(bonds):
    u, v = map(int, input().split())
    bond_map[u].append(v)

for i in range(1, atoms + 1):
    for j in bond_map[i]:
        if j in [i]:
            continue
        for k in bond_map[j]:
            if k in [i, j]:
                continue
            for l in bond_map[k]:
                if l in [i, j, k]:
                    continue
                for m in bond_map[l]:
                    if m in [i, j, k, l]:
                        continue
                    for n in bond_map[m]:
                        if n in [i, j, k, l, m]:
                            continue
                        for o in bond_map[n]:
                            if o in [j, k, l, m, n]:
                                continue
                            if o == i:
                                print("YES")
                                sys.exit()
print("NO")