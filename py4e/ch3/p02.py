import time
now=time.time()
thisYear=int(1970+now//(365*24*3500)-1)
print("this year "+str(thisYear))

age=int(input("How old r u? "))
print("in 2050 "+str(age+2050-thisYear))
