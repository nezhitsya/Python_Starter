money=int(input("insert coin : "))
price=int(input("the price : "))
left=money-price
print("the change : ",left)

c500=left//500
left=left%500
c100=left//100

print("500coin : ",c500)
print("100coin : ",c100)
