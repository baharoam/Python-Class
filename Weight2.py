Vazne1=int(input("Vazne aval? "))
Vazne2=int(input("Vazne dovom? "))
Vazne3=int(input("Vazne sevom? "))
Vazne4=int(input("Vazne chaharom? "))
Vazne5=int(input("Vazne panjom? "))

if(Vazne1>Vazne2):
    if(Vazne1>Vazne3):
        maxi=Vazne1
        str= "vazne 1 is max"
    elif(Vazne1==Vazne3):
       mini=Vazne2
       str = "vazne 2 , min"
        
elif(Vazne2>Vazne1):
     if(Vazne2>Vazne3):
        maxi=Vazne2
        str= "vazne 2 , max"
     elif(Vazne2==Vazne3):
       mini=Vazne1
       str = "vazne 1 , min"
elif(Vazne1==Vazne2):
    if(Vazne3>Vazne4):
        if(Vazne3>Vazne1):
            maxi=Vazne3
            str= "vazne 3 , max"
        elif(Vazne3==Vazne1):
            mini=Vazne4
            str = "vazne 4 , min"
         
    elif(Vazne4>Vazne3):
         if(Vazne4>Vazne1):
            maxi=Vazne4
            str= "vazne 4 , max"
         elif(Vazne4==Vazne1):
            mini=Vazne3
            str = "vazne 3 , min"
    elif(Vazne3==Vazne4):
        if(Vazne5>Vazne3):
            maxi=Vazne5
            str= "vazne 5 , max"
        elif(Vazne5<Vazne3):
            mini=Vazne5
            str = "vazne 5 , min"
print(str)

