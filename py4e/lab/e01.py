d={'a':10, 'b':1, 'c':22}
lst=d.keys()
print(lst)
lst=sorted(lst)
for key in lst :
    print(key,d[key])

print(sorted(d.items()))
