import sys
args = sys.argv

f = open(args[1],"r",encoding = "utf-8")
string = f.read()
f.close

g = open(args[2],"w",encoding = "utf-8")
g.write(string)
g.close

