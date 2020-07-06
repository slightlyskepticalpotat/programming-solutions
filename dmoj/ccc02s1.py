pink, green, red, orange, total = int(input()), int(input()), int(input()), int(input()), int(input())
ways, minimum = 0, 1024
for i in range(total//pink+1):
    for j in range(total//green+1):
        for k in range(total//red+1):
            for l in range(total//orange+1):
                if i*pink + j*green + k*red + l*orange == total:
                    print("# of PINK is {pink} # of GREEN is {green} # of RED is {red} # of ORANGE is {orange}".format(pink=i, green=j, red=k, orange=l))
                    ways += 1
                    if i + j + k + l < minimum:
                        minimum = i + j + k + l
print("Total combinations is {ways}.".format(ways=ways))
print("Minimum number of tickets to print is {minimum}.".format(minimum=minimum))