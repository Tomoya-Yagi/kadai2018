import sys
args = sys.argv
f = open(args[1],"r",encoding = "utf-8")
g = open('grep_' + args[1],"w",encoding = "utf-8")
for line in f:
    if " " + args[2] + " " in line:
       print(line, end = "\n ")
       g.write(f.readline())
g.close
f.close
