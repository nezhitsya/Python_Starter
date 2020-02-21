fname=input('Enter file name : ')
try :
    fhand=open(fname)
except :
    print("File cannot be open")
    quit()

count=dict()
for line in fhand :
    line=line.rstrip()
    if line.startswith('From') :
        wds=line.split()
        if len(wds)>2 :
            if wds[2] in count :
                count[wds[2]]=count[wds[2]]+1
            else :
                count[wds[2]]=1
print(count)
