import random
def getRandom() :
    a=input("Enter Alphabet : ")
    b=input("Enter Alphabet : ")
    a1=ord(a)
    b1=ord(b)
    num=random.randint(a1,b1)
    w=chr(num)
    return w

def getRandomUpper() :
    a=getRandom()
    a=a.upper()
    return a

def getRandomLower() :
    a=getRandom()
    a=a.lower()
    return a

def getRandomDigitCharacter() :
    b1=ord('a')
    b2=ord('z')
    num=random.randint(b1,b2)
    return num

def RandomASCII() :
    num=getRandomDigitCharacter()
    word=chr(num)
    return word

print(RandomASCII())
