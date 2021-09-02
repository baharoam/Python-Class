number=int(input("what number?"))
num1=1
num2=1
summ=0
lst=[]
lst.append(num1)
lst.append(num2)
while number>summ:
    summ=num1+num2
    lst.append(summ)
    num1=num2
    num2=summ
lst.pop(-1)
print(lst)
