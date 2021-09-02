import math
f1=open('h2.text','r')
f2=open('fac.txt','w')
lines = f1.readlines()
ls=[]

for index, line in enumerate(lines):
    ls.append(int(line))
doubles=list(map(lambda x:math.factorial(x), ls))
for i in range(1,len(doubles)):
    massage=f"index : {i} fac: {doubles[i]} \n"
    f2.write(massage)
f1.close()