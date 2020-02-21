def chop(letters) :
    del letters[0]
    del letters[-1]
    return letters

letters=['a','p','p','l','e']
chop(letters)
print(letters)
