import sys
args = sys.argv
f = open(args[1],"r",encoding = "utf-8")

words = {}
for line in f:
    for word in line.split():
        words[word] = words.get(word, 0) + 1

d = [(v,k)for k,v in words.items()]
f.close

d.sort()
d.reverse()
g = open('top10_' + args[1],"w",encoding = "utf-8")
for count, word in d[:10]:
    g.write(str(count) + " " + str(word) + "\n")
g.close
