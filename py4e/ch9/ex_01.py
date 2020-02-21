fhand=open('words.txt')
count=dict()
for line in fhand :
    line=line.rstrip()
    wds=line.split()
    for word in wds :
        if word not in count :
            count[word]=1
        else :
            count[word]+=1
print(count)
