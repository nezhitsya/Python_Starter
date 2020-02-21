hour=float(input("Enter Hour : "))
rate=float(input("Enter Rate : "))

if hour>40 :
    pay=40*rate+(hour-40)*rate*1.5
else :
    pay=hour*rate
print("Pay : ",pay)
