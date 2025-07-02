str = input("Enter String: ")
maxi = 0
l = str.split()
t =""
for i in l:
    temp = len(i)
    if temp> maxi:
        maxi = temp
        t= i

print(t)