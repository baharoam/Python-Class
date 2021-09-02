import random
f1=open('h2.text','w')
# f1.truncate(0)
for i in range(1,1001):
    a=random.randrange(1,1001)
    f1.write(str(a))
    f1.write("\n")

f1.close()