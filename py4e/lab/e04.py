filename=input("Enter File name : ").strip()
infile=open(filename,'r')
count=0
for line in infile :
    line=line.rstrip()
    word=line.split(" ")
    for words in word :
        count=count+1
print(count)
