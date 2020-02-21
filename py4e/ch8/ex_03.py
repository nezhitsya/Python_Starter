fname=input('Enter file name : ')
lst=list()
try :
    fhand=open(fname)
except :
    print("File cannot be open")
    quit()

for line in fhand :
    line=line.rstrip()
    wds=line.split()
    for w in wds :
        if w not in lst :
            lst.append(w)
        else :
            continue
lst.sort()
print(lst)
