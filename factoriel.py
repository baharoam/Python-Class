def Factoriel(Num):
    Fac=1
    if Num<0:
      print("")
 
    elif Num==0:
     print("")
    else:
        for i in range(1,Num+1):
           Fac=Fac*i
        print(Fac)
        

n=int(input("Number?"))
Factoriel(n)