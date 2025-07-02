tp = (1,2,3,4,5)
tp[1:3]
# (2, 3)
tp[-1:]
# (5,)
tp[-1::-1]
# (5, 4, 3, 2, 1)


"""checking element present in tuple or not"""
if 1 in tp:
    print("Yes the element present")
else:
    print("Sorry ! Element not present here")

# Yes the element present

tp2 = (1,1,1,2,2,2)
print(tp2.count(1))#3
print(tp.index(4))#returns the numbers index whether 4 is there it will return it index
print(tp2.index(1))#it also returns the index of first encountered element
