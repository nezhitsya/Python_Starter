fname=input("Enter File name : ")
try :
    fhand=open(fname)
except :
    print("File cannot be opned")
    quit()

total=0
count=0
for line in fhand :
    la=line.rstrip()
    if not la.startswith("X-DSPAM-Confidence:") :
        continue
    else :
        lb=la.find(':')
        lc=line[lb+2:]
        ld=float(lc)
        total=total+ld
        count=count+1
print(total/count)
