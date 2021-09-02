number=int(input("number?"))
x=4
ls=[]
ls.append(2)
ls.append(3)
while(number>x):
    for i in range (2,x-1):
        if x%i==0:
             print("nist")
             break
        elif x%i!=0 :
            print(" aval hast")
            ls.append(x)
            break
           
            
    x+=1
print(ls)


   