Vazne1=int(input("Vazne aval? "))
Vazne2=int(input("Vazne dovom? "))
Vazne3=int(input("Vazne sevom? "))
Vazne4=int(input("Vazne chaharom? "))
Vazne5=int(input("Vazne panjom? "))
if(Vazne1>Vazne2 ):
    maxi=Vazne1
    str = "vazne 1 "
elif(Vazne2>Vazne1):
    maxi=Vazne2
    str = "vazne 2 "
elif(Vazne1==Vazne2):
    if(Vazne3==Vazne4):
        maxi=Vazne5
        str = "vazne 5 "
    elif(Vazne3>Vazne4):
        maxi=Vazne3
        str = "vazne 3 "
    elif(Vazne4>Vazne3):
        maxi=Vazne4
        str = "vazne 4 "
print("maximum number is ", maxi , str)

