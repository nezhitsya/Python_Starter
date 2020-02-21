count=0
sum=0
while True :
    a=input("Enter number : ")
    if a!='done' :
        try :
            aa=int(a)
        except :
            print("Invalid input")
        count=count+1
        sum=sum+aa
        continue
    else :
        print(sum,sum/count)
        break
