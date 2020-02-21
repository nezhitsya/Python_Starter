fname=input("Enter file name : ")
if len(fname)<1 :
    fname='mbox-short.txt'
fhand=open(fname)

di=dict()
for line in fhand :
    line=line.rstrip()
    if line.startswith('From ') :
        to=line.find(':')
        time=line[to-2:to]
        di[time]=di.get(time,0)+1

tmp=list()
for k,v in di.items() :
    new=(k,v)
    tmp.append(new)
tmp=sorted(tmp)
for k,v in tmp :
    print(k,v)
