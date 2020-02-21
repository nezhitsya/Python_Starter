word_1="Hello"
word_2="World"
result=list()
for n in range(len(word_1)) :
    a=word_1[n]
    for n in range(len(word_2)) :
        b=word_2[n]
        result.append(a+b)
print(result)
