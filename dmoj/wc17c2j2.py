mu, ou, lu = map(int, input().split())
ms, os, ls = map(int, input().split())
print(min(min(ms // mu, os // ou), ls // lu))