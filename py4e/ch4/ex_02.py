def computepay(hours,rate) :
    if hours>40 :
        pay=40*rate+(hours-40)*rate*1.5
    else :
        pay=hours*rate
    print("Pay : ",pay)
    return pay

hs=input("Enter Hour : ")
try :
    h=float(hs)
except :
    print("Error, please enter numeric input")
    quit()

rs=input("Enter Rate : ")
try :
    r=float(rs)
except :
    print("Error, please enter numeric input")
    quit()

computepay(h,r)
