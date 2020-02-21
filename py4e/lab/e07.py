import string
fname=input('Enter file name : ')
try :
    fhand=open(fname)
except :
    print('File cannot be open')
    quit()

counts=dict()
for line in fhand :
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    word=line.split()
    for words in word :
        if words not in counts :
            counts[words]=1
        else :
            counts[words]+=1

lst=list()
for key,val in counts.items() :
    lst.append((val,key))
lst.sort(reverse=True)
for key,val in lst[:10] :
    print(key,val)
