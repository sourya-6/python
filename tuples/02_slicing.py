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