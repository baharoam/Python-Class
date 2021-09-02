number=int(input("number?"))
ls=[]
lst=[]
for i in range (3,number+1):
    print("i : ", i)
    for j in range(1,i):
        if i%j==0:
            ls.append(j)
    if sum(ls)==i:
        lst.append(i)
        ls.clear()
    else:
         ls.clear()
            
print(lst)
 



