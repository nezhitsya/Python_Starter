max=0
min=0
while True :
    num=input("Enter a number : ")
    if num=='done' :
        print("Maximum : ",max)
        print("Minimum : ",min)
        quit()
    else :
        try :
            nu=int(num)
        except :
            print("Error")
        if nu>max or max==0 :
            max=nu
        if nu<min or min==0 :
            min=nu
