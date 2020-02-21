lst=[]
def fin(n) :
    for m in range(1,n+1):
        if m==1 or m==2 :
            a=1
            lst.append(a)
        else :
            a=lst[m-3]+lst[m-2]
            lst.append(a)
        print(a)

num=int(input("Enter Number : "))
fin(num)
