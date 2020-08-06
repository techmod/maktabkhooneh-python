import collections
my_input=int(input())
tedad=0
ara={}
vorodi=[]
while tedad!=my_input:
    y=input()
    tedad+=1
    vorodi.append(y)
for letter in vorodi:
    if letter in ara:
        ara[letter]+=1
    else:
        ara[letter]=1
for letter in sorted(ara):
    print(letter,ara[letter])