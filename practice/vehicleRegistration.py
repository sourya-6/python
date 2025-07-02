n = input("Enter the Vehicle Number:")
li =[int(x) for x in n]
flag=0
for i in range(0,len(li)-1):
    if(li[i]==li[i+1]-1):
        continue
    else:
        flag =1
        break
if(flag == 0):
    print("Price is 110000")
else:
    flag =0
    for i in range(0,len(li)-1):
        if(l[i]==li[i+1]):
            continue
        else:
            flag = 1
            break

    

