fname=input("Enter file name : ")
try :
    fhand=open(fname)
except :
    print("File cannot be open")
    quit()
    
count=dict()
for line in fhand :
    line.rstrip()
    if line.startswith("From") :
        word=line.split()
        if len(word)>3:
            if word[1] in count :
                count[word[1]]=count[word[1]]+1
            else :
                count[word[1]]=1
maxk=0
maxv=0
for key,value in count.items() :
    if maxv<value :
        maxk=key
        maxv=value
print(maxk,maxv)
