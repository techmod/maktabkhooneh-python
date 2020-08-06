import math
number=int(input())
tedad=0
list1=[]
while tedad != number :
 x=int(input())
 x=abs(x)
 tedad +=1
 a=math.sqrt(x)
 b=('%.15f'%a)
 list1.append(b[:-11])
for i in range (len(list1)):
    print(list1[i])