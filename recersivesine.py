import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
def calcFac(x): #
    if x == 1 or x == 0: return 1
    val = 1
    for i in range(2, x+1):
        val = val * i
    return val

def sinApprox(angle, terms):
    mult = 1
    if terms % 2 == 0: mult = -1

    power = 2*terms - 1
    val = angle ** power
    val = mult * val/calcFac(power)

    if terms == 1:
         return val
    else:
         return val + sinApprox(angle, terms - 1)



angle = int(input("Enter the angle to approximate (in radians): "))
terms = int(input("Enter the amount of terms to compute: "))
print(sinApprox(angle, terms))
print(math.sin(angle))
plt.plot(angle,sinApprox(angle, terms),'g*')

plt.show() 
