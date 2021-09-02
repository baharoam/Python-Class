import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
def deg2rad(deg):
    
     return math.pi*deg/180
x=[i for i in range(0,361,10)]
y=[math.sin(deg2rad(i)) for i in x ]
plt.plot(x,y,'g*') 
plt.plot(10,4,'rD')
plt.show()
x=list(range(361))
y=list(map(lambda a : math.sin(deg2rad(a)),x))
plt.plot(x,y,'g*') 
plt.plot(10,4,'rD')

plt.show() 