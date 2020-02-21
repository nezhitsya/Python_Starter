hour=input("Enter Hour : ")
try :
    h=float(hour)
except :
    print("Error, please enter numeric input")
    quit()

rate=input("Enter Rate : ")
try :
    r=float(rate)
except :
    print("Error, please enter numeric input")
    quit()

if h>40 :
    pay=40*r+(h-40)*r*1.5
else :
    pay=h*r
print("Pay : ",pay)
