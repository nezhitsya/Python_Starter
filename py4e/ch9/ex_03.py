fname=input("Enter file name : ")
try :
    fhand=open(fname)
except :
    print("File cannot be open")
    quit()

count=dict()
for line in fhand :
    line=line.rstrip()
    if line.startswith('From') :
        word=line.split()
        if len(word)>3 :
            wds=word[1]
            if wds in count :
                count[wds]=count[wds]+1
            else :
                count[wds]=1
print(count)
