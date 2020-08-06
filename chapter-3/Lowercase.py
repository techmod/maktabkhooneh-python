word=str(input())
upper=0
lower=0
for i in word:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
if upper>lower:
    print(word.upper())
else:
    print(word.lower())