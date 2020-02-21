word=input("Enter word : ")
def count(word) :
    count=0
    for letter in word :
        if letter=='a' :
            count=count+1
    print(count)

count(word)
