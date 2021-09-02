 number=int(input("number?"))
ls=[]
s=''
while number//2!=0:
     ls.append(number%2)
     number=number//2
ls.append(1)
print("len : " , len(ls))
for i in range(len(ls)):

     s+=str(ls[i])

print(s[::-1])

#print(bin(46))
