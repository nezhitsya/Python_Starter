fname=input("Enter file name : ")
fhand=open(fname)

di=dict()
for line in fhand :
    line=line.strip()
    line=line.lower()
    for x in line :
        if x.isalpha() is True :
            di[x]=di.get(x,0)+1
        else :
            continue
for f, al in (sorted([(v,k) for k,v in di.items()],reverse=True)) :
    print(f,al)
