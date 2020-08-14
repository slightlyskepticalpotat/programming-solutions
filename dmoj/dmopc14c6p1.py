# the entire sheppard line is a myth, really

stations = []
for i in range(int(input())):
    stations.append(input().strip())

try:
    stations = stations[min(stations.index("Leslie"), stations.index("Bayview")):max(stations.index("Leslie"), stations.index("Bayview"))+1]
    if stations == ["Leslie", "Bessarion", "Bayview"] or stations == ["Bayview", "Bessarion", "Leslie"]:
        print("Y")
    else:
        print("N")
except:
    print("N")