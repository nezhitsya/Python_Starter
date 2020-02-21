max=0
min=0
while True :
    a=input("Enter number : ")
    if a!='done' :
        try :
            aa=int(a)
        except :
            print("Invalid input")
        if max==0 or max<aa :
            max=aa
        else :
            min=aa
        continue
    else :
        print(max,min)
        break
