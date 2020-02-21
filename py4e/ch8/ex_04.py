fname=input('Enter file name : ')
count=0
lst=list()
try :
    fhand=open(fname)
except :
    print("File cannot be open")
    quit()

for line in fhand :
    if line.startswith('From ') :
        line=line.rstrip()
        la=line.split()
        count=count+1
        wds=la[1]
        to=wds.find('@')
        wd=wds[:to]
        if wd not in lst :
            lst.append(wd)
print(lst)
print(count)
