def computegade(s) :
    if s>1.0 or s<0.0 :
        grade="Bad score"
    elif s>=0.9 :
        grade="A"
    elif s>=0.8 :
        grade="B"
    elif s>=0.7 :
        grade="C"
    elif s>=0.6 :
        grade="D"
    elif s<0.6 :
        grade="F"
    print(grade)

score=input("Enter Score : ")
try :
    ss=float(score)
except :
    print("Bad score")
    quit()

computepay(ss)
