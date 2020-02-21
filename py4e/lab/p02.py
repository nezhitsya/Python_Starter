s=0
for i in range(1,21) :
    if i%2==1 :
        continue
    s=s+i
    print("i : ",i,"s : ",s)
    if s>30 :
        break
print("i : ",i,"s : ",s)
