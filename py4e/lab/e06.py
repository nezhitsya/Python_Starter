text='lectopia'
for i in range(len(text)-1,-1,-1) :
    print(text[i],end=" ")
print()

cnt=len(text)
while(cnt>0) :
    cnt=cnt-1
    print(text[cnt],end=" ")
print()

for i in text[::-1] :
    print(i,end=' ')
print()

for i in reversed(text) :
    print(i,end=" ")
