import random
a=1
b=99
hads=random.randint(a,b)
print(hads)
javab=str(input('please enter your javab: '))
while javab!='d':
    if javab=='b':
        a=hads
        hads = random.randint(a, b)
        print(hads)
        javab = str(input('please enter your javab: '))
    elif javab =='k':
        b=hads
        hads = random.randint(a, b)
        print(hads)
        javab = str(input('please enter your javab: '))

