n=int(input("adade fard : "))

for i in range(1,n+2,2):
    print(((n-i)//2)*" "+i*"*"+((n-i)//2)*" " )
    
for j in range(n-2,0,-2):
    print(((n-j)//2)*" "+j*"*"+((n-j)//2)*" " )
