import sys
args = sys.argv
f = open(args[1],"r",encoding = "utf-8")
g = open('tr_' + args[1],"w",encoding = "utf-8")
for line in f:
    line = line.split()
    line = '\n'.join(line)
    line = line.strip()
    line = line + '\n'
    g.write(line)
g.close
f.close
