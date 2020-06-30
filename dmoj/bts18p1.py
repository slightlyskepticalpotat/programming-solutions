import sys
input = sys.stdin.readline

ree1 = [char for char in input().strip()]
ree2 = [char for char in input().strip()]
diff = int(input())
diffs = 0
try: 
     for i in range(len(ree1)):
          if ree1[i] == " " and ree2[i] != " ":
               print("No plagiarism")
               raise
          elif ree2[i] == " " and ree1[i] != " ":
               print("No plagiarism")
               raise
          else:
               if ree1[i] != ree2[i]:
                    diffs+=1
     if diffs <= diff:
          print("Plagiarized")
     else:
          print("No plagiarism")
except:
     pass