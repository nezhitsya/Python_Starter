def a1(a,b) :
    return a+b
def a2(a,b) :
    return a-b
def a3(a,b) :
    return a*b
def a4(a,b) :
    return a/b
a=int(input("첫번째 값 : "))
b=int(input("두번째 값 : "))
print(a,"+",b,"=",a1(a,b))
print(a,"-",b,"=",a2(a,b))
print(a,"*",b,"=",a3(a,b))
print(a,"/",b,"=",a4(a,b))
