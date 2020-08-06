num=0
lst = []
second=[]
while num != -1:
    num = int(input())
    lst.append(num)
ls2=lst.copy()
ls2.remove(max(ls2))
print(max(lst),max(ls2))


