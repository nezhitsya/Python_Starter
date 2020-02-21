for i in range(1,6) :
    for i in range(1,5) :
        print("*",end=" ")
    print('\n')

for i in range(1,6) :
    for i in range(1,1+i) :
        print("*",end=" ")
    print('\n')

for i in range(1,6) :
    for a in range(1,6-i) :
        print(" ",end=" ")
    for b in range(1,i+1) :
        print("*",end=" ")
    print('\n')

for i in range(1,6) :
    for a in range(1,6-i) :
        print(" ",end=" ")
    for b in range(1,i+1) :
        print("*",end=" ")
    for c in range(1,i) :
        print("*",end=" ")
    print('\n')
