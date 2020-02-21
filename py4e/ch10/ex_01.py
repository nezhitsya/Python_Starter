fname=input("Enter file name : ")
if len(fname)<1 :
    fname='mbox-short.txt'
fhand=open(fname)

di=dict()
for line in fhand :
    line=line.rstrip()
    if line.startswith('From ') :
        wd=line.split()
        to=wd[1].find('@')
        wds=wd[1]
        word=wds[to+1:]
        di[word]=di.get(word,0)+1

tmp=list()
for k,v in di.items() :
    new=(v,k)
    tmp.append(new)
tmp=sorted(tmp,reverse=True)
max=0
for v,k in tmp :
    if max<v :
        max=v
        print(k,v)
    else :
        continue
